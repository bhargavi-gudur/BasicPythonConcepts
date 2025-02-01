# check positive and negative number 
num = int(input('enter the value '))
while True :
    if num > 0:
     print('positive :',num)
     break
    elif num < 0 :
      print('negitive : ',num)
      break
    else :
        if num  == 0 :
          print(' exiting from the loop ')
          break

    