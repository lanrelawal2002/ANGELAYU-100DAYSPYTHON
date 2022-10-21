
student_heights = input("Input a list of student hieght. ").split()
for k in range(0, len(student_heights)):
    student_heights[k] = int(student_heights[k])

total_height = 0
for height in student_heights:
    total_height += height
# print(total_height)

number_of_students = 0
for students in student_heights:
    number_of_students += 1
# print(number_of_students)

average_height = round(total_height / number_of_students)
print(average_height)
