while True:
    print("Body Mass Index Calculation Program")
    weight = int(input("Please enter your weight in kg"))
    height = int(input("Please enter your height in cm "))
    bodymass = weight/(height*height)*10000

    if (bodymass <= 25) and (bodymass >= 20):
        print("Your Body Mass Index is Normal", int(bodymass))
    elif (bodymass >= 25) and (bodymass <= 30):
        print("Your Body Mass Index is Overweight", int(bodymass))
    elif (bodymass >= 30) and (bodymass <= 60):
        print("Your Body Mass Index is Obese", int(bodymass))
    elif (bodymass <= 20) and (bodymass >= 10):
        print("Your Body Mass Index is Weak", int(bodymass))
    else:
        print("Something gone wrong. Try again")