# pizza order python program 
size = input("what size pizza you want (s/l/m)?")
bill = 0
if size == 's' or size == 's':
    bill =bill+100
    print('small pizza price is 100 rs. ')
elif size == 'M' or size == 'm':
    bill =bill+200
    print('medium pizza price is 200 rs. ')
elif size == 'L' or size == 'l':
    bill =bill+300
    print('large pizza price is 300 rs. ')
else:
    print("invalid command other than (s/l/m). ")

# extra pepperoni pizza

add_peepperoni = input("do you want pepperoni (y/n?")
if add_peepperoni == 'y' or size == 'Y':
    if size == 's' or size == 's':
        bill =bill+30
    else :
         bill =bill+50
#extra chessa for pizza
extra_cheese= input("do you want  (y/n?")
if add_peepperoni == 'y' or size == 'Y':
      if size == 's' or size == 's':
        bill =bill+30
      else:
         bill =bill+50
print(f'your final bill is {bill} rs')

    