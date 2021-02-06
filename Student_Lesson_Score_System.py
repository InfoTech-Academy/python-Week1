'''
Developer: Ersin ÖZTÜRK
Date: 01.02.2020
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
What does program do? : The program takes the student name, surname,
number of lesson, names of lesson, midterm scores and final scores.
And it gives average score and result that specify as "pass" or "failed".
'''

# "Import time" was used for sleep function.
import time

print("Welcome to Student Lesson Score System")
print("======================================")
time.sleep(1)

name = input("\nPlease insert the Student Name:\n")
time.sleep(1)
print("======================================")
time.sleep(1)
surname = input("\nPlease insert the Student Surname:\n")
time.sleep(1)
print("======================================")
time.sleep(1)


number_of_lesson = int(input("\nHow much lesson will you insert:\n"))

lesson_counter=0
lesson_name=[]
lesson_midterm = []
lesson_final = []
lesson_average=[]
lesson_result=[]

while(lesson_counter<number_of_lesson):

    lesson_name.append(input("\nPlease insert the Lesson-" + str(lesson_counter + 1) + " Name: \n"))
    time.sleep(1)
    print("======================================")

    while (True):

        # Midterm variable change every loop.
        midterm=int(input("\nPlease insert the midterm exam score for Lesson-" +str(lesson_counter+1)+" : \n"))

        # if the score given by the user is not valid, it will go to "while" loop.
        if (midterm < 0) or (midterm > 100):
            print("\nOPPS!! Please enter a valid score (0-100)")
            continue

        # Midterm score add to "lesson_midterm list"
        lesson_midterm.append(midterm)
        break


    time.sleep(1)
    print("======================================")
    time.sleep(1)

    while (True):

        # final variable change every loop.
        final=int(input("\nPlease insert the final exam for Lesson-" +str(lesson_counter+1)+" : \n"))

        #if the score given by the user is not valid, it will go to "while" loop.
        if (final < 0) or (final > 100):
            print("\nOPPS!! Please enter a valid score (0-100)")
            continue
        # Final score add to "lesson_midterm list"
        lesson_final.append(final)
        break
    time.sleep(1)
    print("======================================")
    time.sleep(1)

    lesson_average.append((lesson_midterm[lesson_counter]*0.4)+(lesson_final[lesson_counter]*0.6))
    if lesson_average[lesson_counter] <= 50:
        lesson_result.append("FAILED")
    else:
        lesson_result.append(("PASSED"))


    lesson_counter+=1

print("\n================RESULTS FOR "+name,surname+"======================\n")

lesson_counter=0
while(lesson_counter<number_of_lesson):
    print(lesson_name[lesson_counter]+"     Score::     "+str(lesson_average[lesson_counter])+"     Result: "+ lesson_result[lesson_counter] )
    lesson_counter += 1

