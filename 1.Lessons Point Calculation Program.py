#===========================LESSONS POINT CALCULATION ===================================================
# Developer: Cemil Tepecik
# Date:01.02.2021
# Name, Surname, Student Number, 4 lesson names, midterm and final grades
# will be requested from the user. The 40% of the midterm grade and 60% of the final are taken to calculate
# the year-end average. If the average is less than 50, "FAILED" will be written
# on the screen, and if 50 and above, "PASSED" will be written on the screen.
# This printing process will be done in 4 lessons and the lessons will be printed one after the other.)
#------------------------INITIAL PART---------------------------------
digits=[0,1,2,3] #for loop counter
lectures=['Maths','Computer','Pyhsics','Chemistry']
name = input('Enter the name of student:\n')
surname = input('Enter the surname of the student\n')
number = input('Enter the number of the student\n')
student_info=[name, surname, number] # all informations are gathered on this list

#----------------------MAIN PROGRAM--------------------------------------
# Enter the grades
for i in digits:
    student_info.append(lectures[i])
    midterm=int(input('Enter midterm grade of '+lectures[i]+':\n'))
    final = int(input('Enter final grade of '+lectures[i]+':\n'))
    result_grade=round(0.4*midterm+0.6*final)
    student_info.append(result_grade)
    # Determine the grades!
    if int(result_grade)>=50:
        result='passed'
    else:
        result ='failed'
    student_info.append(result)

#------------------------FINAL PART : Printing the Transcript---------------------------------------------------
#print(student_info)
print('========================')
print('1997-8 SPRING TRANSCRIPT')
print('Name    :',name,'\nSurname :',surname, '\nNumber  :',number)
print('------------------------')
print('1.',student_info[3],'   ',student_info[4],student_info[5])   #Maths
print('2.',student_info[6],'',student_info[7], student_info[8])     #Computer
print('3.',student_info[9],' ',student_info[10], student_info[11])  #Pyhsics
print('4.',student_info[12], student_info[13], student_info[14])    #Chemistry
print('========================')
#========================================END==========================================

#=======OUTPUT========
#1997-8 SPRING TRANSCRIPT
#Name    : Deniz
#Surname : Gezmis
#Number  : 87734343
#------------------------
#1. Maths     51 passed
#2. Computer  73 passed
#3. Pyhsics   95 passed
#4. Chemistry 29 failed
#========================