# @file array_delete_demo.py
# @author Gandla Bhargavi
# @brief Simulates C++ new[] and delete[] behavior in Python
#
# This program demonstrates how Python automatically
# manages memory using garbage collection when a list
# of objects is deleted.
#
# @version 0.1
# @date 2025-09-23

class Base:
    def __init__(self, value):
        self.value = value
        print(f"Constructor: Base({self.value}) created")

    def __del__(self):
        print(f"Destructor: Base({self.value}) destroyed")


def main():
    n = 5
    print("Creating array of objects...")
    bp = [Base(i) for i in range(n)]   # like new Base[n]

    print("\nNow deleting the entire array...")
    del bp   # like delete[] bp in C++

    print("End of program.")


if __name__ == "__main__":
    main()