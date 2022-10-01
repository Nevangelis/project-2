students_grades = open("Project2.txt")
for students in students_grades.readline():
    rules = students.strip().split(":")
    print(f"ID, {rules[0]}, GPA, {rules[2]}")