import math
from dataclasses import dataclass


K_STANDARD_INVERSE = 0.14
ALPHA_STANDARD_INVERSE = 0.02


def idmt_operate_time(current_a, pickup_a, tms, k=K_STANDARD_INVERSE, alpha=ALPHA_STANDARD_INVERSE):
    """
    IEC Standard Inverse IDMT operating time.

    Formula:
    t = TMS * k / ((I / Is)^alpha - 1)
    """
    if current_a <= pickup_a:
        return math.inf

    multiple = current_a / pickup_a
    return tms * k / ((multiple ** alpha) - 1)


@dataclass
class RelaySettings:
    pickup_a: float = 300.0
    tms: float = 0.10
    high_set_a: float = 4000.0
    high_set_delay_s: float = 0.05
    curve_name: str = "IEC Standard Inverse"


@dataclass
class RelayState:
    pickup: bool = False
    trip: bool = False
    blocked: bool = False
    operate_progress: float = 0.0
    high_set_timer_s: float = 0.0
    trip_reason: str = ""


class OvercurrentRelay:
    """
    Simplified low-voltage demonstrator relay engine.

    Functions modelled:
    - 51 IDMT overcurrent
    - 50 high-set instantaneous/short-delay overcurrent
    - permissive/block input
    - trip latch
    - manual reset

    This is not protection-class firmware.
    """

    def __init__(self, settings=None):
        self.settings = settings or RelaySettings()
        self.state = RelayState()

    def reset(self):
        self.state = RelayState()

    def process_sample(self, current_a, dt_s, permissive=True):
        """
        Process one current sample.

        current_a: simulated/measured primary current
        dt_s: sample interval in seconds
        permissive: if False, trip is blocked
        """
        if self.state.trip:
            return self.state

        self.state.blocked = not permissive
        self.state.pickup = current_a > self.settings.pickup_a

        if not permissive:
            self.state.operate_progress = 0.0
            self.state.high_set_timer_s = 0.0
            return self.state

        # 50 high-set element
        if current_a >= self.settings.high_set_a:
            self.state.high_set_timer_s += dt_s
            if self.state.high_set_timer_s >= self.settings.high_set_delay_s:
                self.state.trip = True
                self.state.trip_reason = "50 high-set overcurrent"
                return self.state
        else:
            self.state.high_set_timer_s = 0.0

        # 51 IDMT element
        if current_a > self.settings.pickup_a:
            operate_time = idmt_operate_time(
                current_a=current_a,
                pickup_a=self.settings.pickup_a,
                tms=self.settings.tms,
            )

            if math.isfinite(operate_time):
                self.state.operate_progress += dt_s / operate_time

            if self.state.operate_progress >= 1.0:
                self.state.trip = True
                self.state.trip_reason = "51 IDMT overcurrent"
                return self.state
        else:
            self.state.operate_progress = 0.0

        return self.state
