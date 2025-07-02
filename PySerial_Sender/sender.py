import serial

ser = serial.Serial('COM8', baudrate=9600, timeout=1)
print("Listening on COM8...")

try:
    while True:
        data = ser.readline().decode(errors='ignore').strip()
        if data:
            print(f"Received: {data}")
except KeyboardInterrupt:
    print("Stopped by user.")
finally:
    ser.close()
