import random
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
count = len(names)
choice = random.randint(0,count-1)
winner = names[choice]

print(f"{winner} is going to buy the meal today!")