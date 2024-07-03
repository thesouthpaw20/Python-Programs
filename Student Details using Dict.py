students = {}
num_students = int(input("Enter the number of students: "))

for _ in range(num_students):
    name = input("Enter name: ")
    roll_no = input("Enter roll number: ")
    total_mark = int(input("Enter total marks: "))
    students[roll_no] = {'name': name, 'total_mark': total_mark}

highest_mark = max(students.values(), key=lambda x: x['total_mark'])
print("Student with highest marks:", highest_mark)
