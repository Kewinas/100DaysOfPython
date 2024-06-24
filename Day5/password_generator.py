import random

letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
    "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H",
    "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y",
    "Z"
]

symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{",
    "}", "|", ";", ":", '"', ",", ".", "<", ">", "?", "/", "~", "`"
]

digits = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

print("Welcome to the Password Generator.")

nr_letters = int(input("How many letters you want in your password?\n"))
nr_symbols = int(input("How many symbols you want in your password?\n"))
nr_digits = int(input("How many digits you want in your password?\n"))

password = []

for char in range(1, nr_letters + 1):
    password += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for char in range(1, nr_digits + 1):
    password += random.choice(digits)

random.shuffle(password)
password_done = "".join(password)

print(f"Your password is: {password_done}")