# Function to calculate the number of days, 
# months, weeks, and years left until 
# the age of 90

age = int(input("enter the age "))
# Function to calculate the number of days, months, weeks, and years left until the age of 90
def liveUntilAge():
    year_left = 90 - age
    days_left = year_left*365
    months_left = year_left*12
    weeks_left = year_left * 52
    print(
        f"my current age {age} ,yearsleft {year_left},days_left {days_left},months_left {months_left},weeks_left {weeks_left} .")

# Call the function to execute it
liveUntilAge()
