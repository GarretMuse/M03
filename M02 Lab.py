# Garret Muse
# M02 Lab
# This app tests if students qualify for the Dean's list or Honor Roll
students = []
student = []
student_last_name = ""
student_first_name = ""
student_gpa= ""

while student_last_name != "ZZZ":
    student_last_name = input("Enter student's last name: ")
    
    if student_last_name != "ZZZ":
         student.append(student_last_name)
         student_first_name = input("Enter student's first name: ")
         student.append(student_first_name)
         student_gpa = input("Enter student's GPA: ")
         student.append(student_gpa)
         students.append(student)
         student = []
    
    print(students)

for i in range(len(students)):
    if float(students[i][2]) >= 3.5:
        print("Congratulations! " + students[i][1] + " qualifies to make the Dean's list.")
    
    elif float(students[i][2]) >= 3.25:
        print("Congratulations! " + students[i][1] + " qualifies to make Honor Roll.")

    else:
        print(students[i][1] + " does not qualify for any list.")