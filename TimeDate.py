"""
@file TimeDate.py
@author Gandla Bhargavi
@brief Program to display the current date and time in Python.

@date 2025-11-24
"""

from datetime import datetime

def main():
    now = datetime.now()  # get current date & time

    # Format: DD-MM-YYYY  HH:MM:SS
    date_time = now.strftime("%d-%m-%Y  %H:%M:%S")

    print("\n--- Current Date and Time ---")
    print("Date & Time :", date_time)

if __name__ == "__main__":
    main()