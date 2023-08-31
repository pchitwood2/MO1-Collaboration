#Peyton Chitwood

#MO2LAB_CaseStudyAPP.py

#This application checks students. Users enter a last name and first name
#for the student. If last name is ZZZ, the program quits. Users will also enter
#GPA of students, and the GPAs are compared to see if the student makes the 
#Dean's List or Honor Roll.


while True:
    lastName = input("Enter student's LAST name:")
    if lastName == 'ZZZ':
        print("PROCESS STOPPED")
        break
    firstName = input("Enter student's FIRST name:")
    GPA = float(input("Enter GPA:"))
    if GPA > 3.5:
        print(firstName + " " + lastName + " has made the Dean's List")
    elif GPA > 3.25 and GPA < 3.5:
        print(firstName + " " + lastName + " has made the Honor Roll")
    else:
        print(firstName + " " + lastName + " has a GPA of " + str(GPA))