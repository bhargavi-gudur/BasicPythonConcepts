# practice the nested lists within lists.

#timetable.
timetable =[["math","english","history"],
            ["science","math","art"],
            ["english","physic","music"],
            ["history","science","math"],
            ["cs","math","music"]]

#display the timetable
day =["mon","tue","wed","thurs","fri"]

# len(timetable): This gives the total number of days, which is 5 in this case.
# range(len(timetable)): This generates indices 0, 1, 2, 3, and 4.
# for i in range(len(timetable)): This loop iterates over these indices, allowing us to access each sub-list (each day's subjects) using timetable[i].
for i in  range (len(timetable)):
    print(f"{day[i]}:{timetable[i]}")