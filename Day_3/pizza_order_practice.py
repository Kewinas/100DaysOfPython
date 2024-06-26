size = input()
add_pepperoni = input()
extra_cheese = input()

bill = 0

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  if size == "M" or size == "L":
    bill += 3

if extra_cheese == "Y":
  bill += 1

if size == "S":
  bill += 15
if size == "M":
  bill += 20
if size == "L":
  bill += 25

print(f"Galutinė suma: ${bill}.")