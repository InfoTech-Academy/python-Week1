courseList=[]
midTermList=[]
finalList=[]
number=1
passed="passed"
failed="failed"
name= input("Please write your name:")
surName=input("Please write your surname:")
studentNumber=input("Please write your student number:")
while number<=4:
    courseName = input("Please write your course name:")
    courseList.append(courseName)
    midTermPoint = float(input("Please, enter your mid-term point :"))
    midTermList.append(midTermPoint)
    finalPoint = float(input("Please, enter your final point :"))
    finalList.append(finalPoint)
    if ((midTermPoint<0) or (midTermPoint>100)) or ((finalPoint<0) or (finalPoint>100)):
        print("Please enter a valid value for  midterm or final points")
        continue
    else:
        number+=1

print("Student informations:")
print(surName.upper(), name.upper(), studentNumber)
print("Course Grades")
number=0
for number in range(4):
    calculation = (midTermList[number] * 0.40) + (finalList[number] * 0.60)

    if calculation<50:
        print(courseList[number], calculation, failed)
    elif (calculation >= 50) and (calculation <= 100):
        print(courseList[number], calculation, passed)
    else:
        print("You have a mistake!")