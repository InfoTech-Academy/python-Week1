while True:
    key = int(input("Please enter a number 1 key to calculate a body index or any integer key to break :"))
    if key==1:
        while True:
            length= float(input("Please enter your length as meter unit (185cm=1.85m):"))
            if 0<length<3:
                break
            else:
                print("You have a mistake. Please try again.")
                continue
        weight= float(input("Please enter your weight as kg unit  :"))
        bodyIndex= int(weight//(length**2))
        print(bodyIndex)
        if bodyIndex<25:
            print("FIT") 
        elif (bodyIndex>=25) and (bodyIndex<30):
            print("FAT")
        elif (bodyIndex>=30) and (bodyIndex<40):
            print("OBESE")
        elif bodyIndex>=40:
            print("ROTUND")
        else:
            print("THIN")
            continue
    elif key!=1:
        break
