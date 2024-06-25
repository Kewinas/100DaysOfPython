student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for score in student_scores:
  if 91 <= student_scores[score] <= 100:
    student_grades[score] = "Outstanding"
  if 81 <= student_scores[score] <= 90:
    student_grades[score] = "Exceeds Expectations"
  if 71 <= student_scores[score] <= 80:
    student_grades[score] = "Acceptable"
  if student_scores[score] <= 70:
    student_grades[score] = "Fail"

print(student_grades)