student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

count = 0
sum = 0
for height in student_heights:
    count += 1
    sum += height
    average = round(sum / count)

print(f"total height = {sum}")
print(f"number of students = {count}")
print(f"average height = {average}")