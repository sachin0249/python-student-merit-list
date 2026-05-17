# Python program to display merit list using tuples

students = []

n = int(input("Enter number of students: "))

# Taking input for student name and CGPA
for i in range(n):
    name = input("Enter student name: ")
    cgpa = float(input("Enter CGPA: "))

    students.append((name, cgpa))

# Sorting tuples based on CGPA in ascending order
students.sort(key=lambda x: x[1])

# Displaying sorted merit list
print("\nMerit List (Ascending Order of CGPA):")

for student in students:
    print(student)
