print("Welcome to the treasure island. Your mission is to find the treasure.")

direction = input("Which side you want to go? Left or Right?")
if direction == "Left":
    swim = input("You will want to swim or wait? Swim or Wait?")
    if swim == "Wait":
        door = input("Which color door will you choose? Red, Yellow or Blue?")
        if door == "Yellow":
            print("You win!")
        if door == "Red" or door == "Blue":
            print("Game over.")
    else:
        print("Game over.")
else:
    print("Game over.")