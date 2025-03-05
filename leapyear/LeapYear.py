# leap year sample program using fun method in python.
# leap year is a year, occurring once every four years, which has 366 days including 29 February as an intercalary day.
year = int(input("enter the year? to find leap year are not:  "))

def leapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f" 1: it is a {year} leap year")
            else:
                print(f" 1: it is  {year} not a leap year")
        else:
          print(f"2:it is a {year}  leap year")
    else:
        print(f"2:it is  {year} not a leap year")


leapYear(year)
