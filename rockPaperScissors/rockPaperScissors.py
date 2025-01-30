# project playing a game rock paper scissors .
#import random inbuilt function.
import random as rd
user_choice =int(input("enter the rock-0,scissor-1,paper-2 ? :"))
computer_choice = rd.randint(0,2)
print("computer choice :",computer_choice )

#invalid number user entered 
if user_choice >2 or user_choice < 0 :
    print("invalid number.")

# rock wins against scissor.
# scissors win against paper.
# paper wins against rock.
else :
    if computer_choice == user_choice:
        print(" it's a draw.")
    elif computer_choice == 0 or user_choice==2:
      print(" you lose.")  
    elif user_choice ==0 or computer_choice==2:
      print(" you win.")
    elif computer_choice > user_choice:
        print(" you lose.")
    elif user_choice > computer_choice:
        print(" you win.")
    



