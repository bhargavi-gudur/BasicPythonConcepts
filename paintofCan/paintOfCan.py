# Purpose: To calculate the number of paint cans required to paint a wall
# author : gandla bhargavi
# version: python 3.6
import math
h = int(input("enter the height  of wall in meters :\n"))
w = int(input("enter the width  of wall in meters :\n"))
coverage = 7


def paint_can(h, w, coverage):
    area = h*w
    no_of_Cans = math.ceil(area/coverage)
    print(f"area ->{area},number of cans ->{no_of_Cans} paints")


paint_can(h, w, coverage)
