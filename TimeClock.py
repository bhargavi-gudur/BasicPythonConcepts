"""
@file TimeClock.py
@author Gandla
@brief Program to display current time and run a live digital clock.

@date 2025-12-01
"""

import time
from datetime import datetime

def show_current_time():
    now = datetime.now()
    print("Current Time :", now.strftime("%H:%M:%S"))

def digital_clock():
    print("\n--- Live Digital Clock (Press CTRL+C to stop) ---")
    while True:
        now = datetime.now()
        print(now.strftime("%H:%M:%S"), end="\r")
        time.sleep(1)

def main():
    show_current_time()   # show one-time current time
    digital_clock()       # start live clock

if __name__ == "__main__":
    main()