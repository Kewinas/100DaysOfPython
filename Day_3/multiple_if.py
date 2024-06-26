# Elif
height = int(input("Koks tavo ūgis?"))

if height > 120:
    print("Gali eiti į atrakcionus.")
    age = int(input("Koks tavo amžius?"))
    if age < 12:
        bill = 5
    elif age > 18:
        bill = 12
    else:
        bill = 7
    photos = input("Ar reikės nuotraukų?")
    if photos == "Taip":
        bill += 3
        print(f"Jums reikia sumokėti ${bill}.")
    if photos == "Ne":
        print(f"Jums reikia sumokėti ${bill}.")
else:
    print("Esi per žemas, bandyk kitą kartą.")