import serial
import time

# Open COM3 for writing (linked to COM4 via com0com)
ser = serial.Serial('COM3', baudrate=9600, timeout=1)

print("Sending data to COM3... (watch COM4 in PuTTY)")

try:
    while True:
        ser.write(b"Hello from virtual STM32!\r\n")
        print("Sent: Hello from virtual STM32!")
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped by user.")

finally:
    ser.close()
