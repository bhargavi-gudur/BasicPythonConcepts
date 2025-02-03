#sample python random module
#import random
import random as rd

# randint(a,b)
integer = rd.randint(1,3)
print("RANDOM INTEGER :",integer )

# randrange(a,b)
range = rd.randrange(1,5)
print("RANDOM range :",range )

# random() -> floating point number

# random() -> floating point number
random1 = rd.random()
print("RANDOM FUNCTION:", random1)

# uniform(a, b) -> floating point number between a and b
uniform_value = rd.uniform(1, 10)
print("UNIFORM FUNCTION:", uniform_value)