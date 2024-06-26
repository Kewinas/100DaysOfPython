import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

hands = [rock, paper, scissors]
choice = int(input("Ka renkiesi: 0 - Akmeni, 1 - Popieriu, 2 - Zirkles?"))
computer = random.randint(0, 2)

if (choice == 0 and computer == 2) or (choice == 1 and computer == 0) or (choice == 2 and computer == 1):
    print("Tu pasirinkai:")
    print(hands[choice])
    print("Kompiuteris pasirinko:")
    print(hands[computer])
    print("Laimejai!")
elif (choice == 2 and computer == 0) or (choice == 0 and computer == 1) or (choice == 1 and computer == 2):
    print("Tu pasirinkai:")
    print(hands[choice])
    print("Kompiuteris pasirinko:")
    print(hands[computer])
    print("Pralaimejai!")
else:
    print("Tu pasirinkai:")
    print(hands[choice])
    print("Kompiuteris pasirinko:")
    print(hands[computer])
    print("Lygiosios!")