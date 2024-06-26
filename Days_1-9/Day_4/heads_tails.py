import random

choices = ["0", "1"]

toss = random.choice(choices)

if toss == "0":
  print("Tails")
if toss == "1":
  print("Heads")