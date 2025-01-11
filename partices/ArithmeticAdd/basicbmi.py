#sample calcuate bmi 
#method1
weight = float(input("enter the weight :"))
height = float(input("enter the height :"))
def cal_bmi(weight,heigth):
    bmi = weight/(heigth ** 2)
    return bmi
bmi = cal_bmi(weight,height)
print("bmi value :",bmi)

    
    
    