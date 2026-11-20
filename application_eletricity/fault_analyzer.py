"""
@file fault_analyzer.py
@brief Analyzes electrical parameters to identify abnormalities.
@date 20/11/2026
"""

def analyze_fault(voltage, current, frequency):
    """
    @brief Analyzes electrical readings for abnormal conditions.
    @param voltage Voltage reading in volts.
    @param current Current reading in amperes.
    @param frequency Frequency reading in hertz.
    """
    fault_detected = False

    print("\n--- FAULT ANALYSIS REPORT ---")

    if voltage < 210:
        print("[WARNING] Undervoltage detected!")
        fault_detected = True

    elif voltage > 240:
        print("[WARNING] Overvoltage detected!")
        fault_detected = True

    if current > 10:
        print("[WARNING] Overcurrent condition detected!")
        fault_detected = True

    if frequency < 49:
        print("[WARNING] Low frequency detected!")
        fault_detected = True

    elif frequency > 51:
        print("[WARNING] High frequency detected!")
        fault_detected = True

    if not fault_detected:
        print("Electrical parameters are within defined limits.")
        print("System Status: NORMAL")
    else:
        print("System Status: ABNORMAL")
        print("Inspection is recommended.")


# Main program
print("ELECTRICITY FAULT PATTERN ANALYZER")

voltage = float(input("Enter voltage (V): "))
current = float(input("Enter current (A): "))
frequency = float(input("Enter frequency (Hz): "))

if voltage <= 0 or current < 0 or frequency <= 0:
    print("Invalid electrical readings.")
else:
    analyze_fault(voltage, current, frequency)