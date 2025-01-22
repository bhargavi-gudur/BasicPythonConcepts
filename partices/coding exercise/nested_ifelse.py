#sample nested if ,else ,elif
weight = float(input("enter the weight in kg  :"))
height = float(input("enter the height in meter  :"))
#calcuate bmi formula
bmi = round(weight/height**2)
#print(BMI)
if bmi<18.5:
    print(f'your bmi is{bmi} and your are underweight')
elif bmi<25:
    print(f'your bmi is{bmi} and your are normalweight')
elif bmi<45:
    print(f'your bmi is{bmi} and your are overweight') 
elif bmi<60:
    print(f'your bmi is{bmi} and your are obsesity')    
else:
    print(f'your bmi is{bmi} and your are clincillay obese')    