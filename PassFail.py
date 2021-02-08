#Furkan Surucu

name = input("Enter your name: ")
surname = input("Enter your surname: ")
student_number = int(input("Enter your student number: "))
courses=[]
midterms=[]
finals=[]
average=[]
i=0
for i in range(4):
    course= input("Enter your course:")
    courses.append(course)
    midterm_not= int(input("Enter the midterm grade of the {} course: ".format(courses[i])))
    midterms.append(midterm_not)
    final_not= int(input("Enter the final grade of the {} course: ".format(courses[i])))
    finals.append(final_not)
    average_not = (float(midterms[i]) * 0.4) + (float(finals[i]) * 0.6)
    average.append(average_not)

print("\nDear",name,surname, "with",student_number,"student number:\n")
for i in range(4):
    if average[i] >= 50:
        print("You passed the",courses[i],"with an average of",average[i],", congratulations.")

    else:
        print("You failed the",courses[i],"with an average of",average[i],", you should study more.")

