'''
Developer: Ersin ÖZTÜRK
Date: 01.02.2020
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
What does program do? : The program takes the name, surname,
weight and height. And it gives Body Mass Index and Classify of BMI.
'''
print("Welcome to Body Mass Index Calculation Programe")
print("======================================")
name = input("\nPlease insert your name:\n")
print("======================================")
surname = input("\nPlease insert your surname:\n")
print("======================================")
weight = int(input("\nPlease insert your weight (kg):\n"))
print("======================================")
height = int(input("\nPlease insert your height (cm):\n"))
print("======================================")

BMI=weight/(height*height*0.0001)

print("Your Body Mass Index (BMI) is ",BMI)

if(BMI<18.5):
    print("\nYour weight is 'THIN'\n")
elif(BMI<25):
    print("\nYour weight is 'NORMAL'\n")
elif(BMI<30):
    print("\nYour weight is 'OVERWEIGHT'\n")
elif(BMI<35):
    print("\nYour weight is 'TYPE-1 OBESITY'\n")
elif(BMI<40):
    print("\nYour weight is 'TYPE-2 OBESITY'\n")
elif(BMI<50):
    print("\nYour weight is 'MORBID OBESITY (SUPER OBESITY)'\n")
else:
    print("\nYour weight is 'MORBID OBESITY (SUPER SUPER OBESITY)'\n")


