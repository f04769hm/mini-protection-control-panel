(*
Mini Protection & Control Panel
CODESYS Opta Structured Text Draft

Purpose:
Low-voltage demonstrator logic for overcurrent pickup, IDMT trip,
high-set trip, permissive/blocking, trip latch, reset and relay healthy output.

This is not protection-class relay firmware.
*)

PROGRAM PLC_PRG

VAR
    // Inputs - map these to physical Opta inputs in CODESYS
    Fault_Test_PB      : BOOL;   // I1 - optional test command
    Reset_PB           : BOOL;   // I2 - reset pushbutton
    Permissive         : BOOL;   // I3 - trip permissive/block switch
    Current_Input_V    : REAL;   // I4 - 0 to 10 V current simulation input

    // Outputs - map these to physical Opta relay outputs in CODESYS
    Trip_Command       : BOOL;   // Q1
    Relay_Healthy      : BOOL;   // Q2
    Pickup_Lamp        : BOOL;   // Q3
    Trip_Lamp          : BOOL;   // Q4

    // Scaled values
    Current_Input_Limited_V : REAL;
    Current_A               : REAL;
    Current_Multiple        : REAL;

    // Settings
    Pickup_A          : REAL := 300.0;
    TMS               : REAL := 0.10;
    High_Set_A        : REAL := 5000.0;
    High_Set_Delay_s  : REAL := 0.05;

    // IEC Standard Inverse constants
    K_StandardInverse     : REAL := 0.14;
    Alpha_StandardInverse : REAL := 0.02;

    // Timing / cycle
    Cycle_Time_s      : REAL := 0.01;   // Assumed 10 ms PLC cycle for first draft
    IDMT_Operate_Time_s : REAL;
    Operate_Progress  : REAL := 0.0;

    // State
    Trip_Latch        : BOOL := FALSE;
    Blocked           : BOOL := FALSE;
    Pickup            : BOOL := FALSE;

    // Timers
    High_Set_Timer    : TON;

    // Internal
    High_Set_Condition : BOOL;
    IDMT_Condition     : BOOL;
END_VAR


// Limit analogue input to expected 0-10 V range
IF Current_Input_V < 0.0 THEN
    Current_Input_Limited_V := 0.0;
ELSIF Current_Input_V > 10.0 THEN
    Current_Input_Limited_V := 10.0;
ELSE
    Current_Input_Limited_V := Current_Input_V;
END_IF;


// Scale 0-10 V to 0-6000 A simulated current
// 0.5 V = 300 A pickup
// 5.0 V = 3000 A = 10x pickup
// 8.33 V approx = 5000 A high-set
Current_A := Current_Input_Limited_V * 600.0;


// Relay healthy output
// First version: energised while logic is running.
// Limitation: this is not a true missing-pulse watchdog.
Relay_Healthy := TRUE;


// Reset logic
IF Reset_PB THEN
    Trip_Latch := FALSE;
    Operate_Progress := 0.0;
    High_Set_Timer(IN := FALSE, PT := T#50MS);
END_IF;


// Permissive / block logic
Blocked := NOT Permissive;


// Pickup logic
Pickup := Current_A > Pickup_A;
Pickup_Lamp := Pickup;


// If blocked, reset timing progress and prevent new trip operation
IF Blocked THEN
    Operate_Progress := 0.0;
    High_Set_Timer(IN := FALSE, PT := T#50MS);
ELSE
    // High-set 50 element
    High_Set_Condition := Current_A >= High_Set_A;

    High_Set_Timer(
        IN := High_Set_Condition,
        PT := T#50MS
    );

    IF High_Set_Timer.Q THEN
        Trip_Latch := TRUE;
    END_IF;


    // IDMT 51 element
    IDMT_Condition := Current_A > Pickup_A;

    IF IDMT_Condition THEN
        Current_Multiple := Current_A / Pickup_A;

        // IEC Standard Inverse:
        // t = TMS * 0.14 / ((I / Is)^0.02 - 1)
        IDMT_Operate_Time_s := TMS * K_StandardInverse / (EXPT(Current_Multiple, Alpha_StandardInverse) - 1.0);

        // Integrating progress method:
        // progress reaches 1.0 when the relay should operate
        IF IDMT_Operate_Time_s > 0.0 THEN
            Operate_Progress := Operate_Progress + (Cycle_Time_s / IDMT_Operate_Time_s);
        END_IF;

        IF Operate_Progress >= 1.0 THEN
            Trip_Latch := TRUE;
        END_IF;
    ELSE
        Operate_Progress := 0.0;
    END_IF;
END_IF;


// Output logic
Trip_Command := Trip_Latch;
Trip_Lamp := Trip_Latch;