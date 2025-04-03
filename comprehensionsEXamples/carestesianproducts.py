cartesian_x = int(input("enter the carestian x value for pairs of points: "))
cartesian_y = int(input("enter the carestian y value for pairs of points: "))
def cartesian_pairs(x,y):
    pairs = [(i,j) for i in range(x) for j in range(y)]
    print(f"The cartesian pairs are:{pairs}")
    

cartesian_pairs(cartesian_x,cartesian_y)
