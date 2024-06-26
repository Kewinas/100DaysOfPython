line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()

coordinates = list(position)
if coordinates[0] == "A":
    pav = 0
if coordinates[0] == "B":
    pav = 1
if coordinates[0] == "C":
    pav = 2

if coordinates[1] == "1":
    line1[pav] = "X"
if coordinates[1] == "2":
    line2[pav] = "X"
if coordinates[1] == "3":
    line3[pav] = "X"


print(f"{line1}\n{line2}\n{line3}")