student_scores = input("Input a list of student scores. ").split()
for k in range(0, len(student_scores)):
    student_scores[k] = int(student_scores[k])
print(student_scores)

lowest_score = 0
starting_score = student_scores[0]
for score in student_scores:
    if score < starting_score:
        lowest_score = score

print(f"The lowest score is {lowest_score}")
