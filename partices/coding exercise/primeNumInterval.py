# generate the prime number in between the intervals
low_val = int(input("enter the low value :"))
high_val = int(input("enter the high value :"))


def prime_num_inter(low, high):
   # is_prime = true
    for num in range(low_val, high_val+1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, num//2 + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=", ")
    print()


prime_num_inter(low_val, high_val)
