student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

average = 0
count = 0
total = 0
for height in student_heights:
    count += 1
    total += height
    average = round(total / count)

print(f"total height = {total}")
print(f"number of students = {count}")
print(f"average height = {average}")
