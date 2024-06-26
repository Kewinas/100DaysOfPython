bill = float(input("Kokia pilna suma? $"))
tip_percent = int(input("Kiek procentų arbatpinigių norite palikti? 10, 12, 15 ar 20?"))
people = int(input("Kiek žmonių pasidalins sąskaita?"))

bill_final = float(bill + (bill * (tip_percent / 100)))
bill_per_person = round(float(bill_final / people), 2)

print(f"Kiekvienas žmogus turi sumokėti po ${bill_per_person}.")