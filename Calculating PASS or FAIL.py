# Developer: Furkan Turkmen
# Date     : 01.02.2021
# Purpose of Software: Reinforcement of learned Python Code and self-improvement.
# what does program do: The program takes the student name, surname, name of lessons, midterm scores and final scores
# and it gives average scores and final scores. Also specify results as "PASS" or "FAILED".

while True:
    print("Welcome to the InfotecAcademy Education System \nIn order for the system to work correctly, "
          "please complete the information requested from you and enter it correctly.")

    name, surname, nu = input("Enter your Name, Surname and Student Number with a space: ").split()
    lesson1, lesson2, lesson3, lesson4 = input("Please Enter the names of the Courses, spacing them every once in a while: ").split()
    v1, v2, v3, v4 = input("Enter the midterm grades of "+lesson1+" "+lesson2+" "+lesson3+" "+lesson4 +" courses with a gap every once in a while: ").split()

    f1, f2, f3, f4 = input("Enter the midterm grades of "+lesson1+" "+lesson2+" "+lesson3+" "+lesson4 +" courses with a gap every once in a while: ").split()

    print("Dear "+name+" "+surname+" " + nu+"\nAs a result of the grades you got from the exams "
    "Your year-end grades are shown below.")

    if (int(v1)*0.4 + int(f1)*0.6 >= 50) and (int(v1)*0.4 + int(f1)*0.6 <= 100):
        print(lesson1+" PASSED", int(int(v1)*0.4 + int(f1)*0.6))
    elif (int(v1)*0.4 + int(f1)*0.6 < 50) and (int(v1)*0.4 + int(f1)*0.6 > 0):
        print(lesson1+" FAILED " + str(int(v1)*0.4 + int(f1)*0.6))
    else:
        print("A problem occurred in " + lesson1 +" class, please try again.")
    if (int(v2)*0.4 + int(f2)*0.6 >= 50) and (int(v2)*0.4 + int(f2)*0.6 <= 100):
        print(lesson2 + " PASSED", int(int(v2)*0.4 + int(f2)*0.6))
    elif(int(v2)*0.4 + int(f2)*0.6 <= 50) and (int(v2)*0.4 + int(f2)*0.6 >= 0):
        print(lesson2 + " FAILED", int(int(v2)*0.4 + int(f2)*0.6))
    else:
        print("A problem occurred in " + lesson2 +" class, please try again.")
    if (int(v3)*0.4 + int(f3)*0.6 >= 50) and (int(v3)*0.4 + int(f3)*0.6 <= 100):
        print(lesson3 + " PASSED", int(int(v3)*0.4 + int(f3)*0.6))
    elif(int(v3)*0.4 + int(f3)*0.6 <= 50) and (int(v3)*0.4 + int(f3)*0.6 >= 0):
        print(lesson3 + " FALILED", int(int(v3)*0.4 + int(f3)*0.6))
    else:
        print("A problem occurred in " + lesson3 +" class, please try again.")
    if (int(v4)*0.4 + int(f4)*0.6 >= 50) and (int(v4)*0.4 + int(f4)*0.6 <= 100):
        print(lesson4 + " PASSED", int(int(v4)*0.4 + int(f4)*0.6))
    elif(int(v4)*0.4 + int(f4)*0.6 <= 50) and (int(v4)*0.4 + int(f4)*0.6 >= 0):
        print(lesson4 + " FAILED", int(int(v4)*0.4 + int(f4)*0.6))
    else:
        print("A problem occurred in " + lesson4 +" class, please try again.")
