n = int(input())
def pattern(n):
    for i in range(n):
        for j in range(n):
            if i == j or i > j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


pattern(n)
