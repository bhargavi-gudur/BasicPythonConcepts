#random inbuilt function using python code.
# when tossing the coin head -1, tails -0.
# using random in built function.

#import random  function.
import random as rd
coin_side=rd .randint(0,2)
print(" tossing the coin random inbuilt function geneat it based , \n below condition it get excuted")
if coin_side ==1:
    print('heads',coin_side)
elif coin_side == 0 :
    print('tail',coin_side)
else:
     print('no sides either head or tail ',coin_side)