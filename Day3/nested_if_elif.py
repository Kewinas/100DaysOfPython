# Elif
height = int(input("Koks tavo ūgis?"))

if height > 120:
    print("Gali eiti į atrakcionus.")
    age = int(input("Koks tavo amžius?"))
    if age < 12:
        print("Kainuos $5.")
    elif age > 18:
        print("Kainuos $12.")
    else:
        print("Kainuos $7.")
else:
    print("Esi per žemas, bandyk kitą kartą.")