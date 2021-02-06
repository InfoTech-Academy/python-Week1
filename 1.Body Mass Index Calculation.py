#============BODY MASS INDEX CALCULATİON =======================================
# Developer: Cemil Tepecik
# Date:02.02.2021
# #The parameter that indicates whether a person's weight is normal according to his height is called Body Mass Index.
# In short, if we divide the weight of a person by the square of the person's height,
# the body mass index comes out. Take the weight and height from the user and write a warning as
# Underweight if the index<18.5; normal if 18.5=< the index < 25, overweight if  25=< the index <30
# obese if  30=< the index <40, # Extreme fat if 40=< the index.
#-----------------------------MAIN-----------------------------------------
weight=float(input('Enter the Weight:\n'))
height=float(input('Enter the Weight:\n'))
index=int((weight//(height**2)))
if index<18:
    print('Your Body Mass Index',index,'you are Underweight; feed better |(')
elif 18 <= index <25:
    print('Your Body Mass Index',index,'you are Normal; super ||')
elif 25<= index<=30:
    print('Your Body Mass Index',index,'you are Overweight; start sport |)')
elif 30<=index<40:
    print('Your Body Mass Index',index,'you are Obese; eat less and start sport |))')
else:
    print('Your Body Mass Index',index,'you are Extremefat; do whatever you want |)))')
#=========================END OF THE PROGRAM===============================================