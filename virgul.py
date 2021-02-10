fruits=["apple","banana","cherry"]
for x in fruits:
    if x == fruits[-1]:
        print(x)
    else:
        print(x,end=",")