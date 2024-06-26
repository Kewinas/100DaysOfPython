import calculator_ascii

print(calculator_ascii.art)


def calculator(first_number, operation, second_number):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        return first_number / second_number
    else:
        return None


operations = ["+", "-", "*", "/"]

while True:
    try:
        first_number = float(input("What is the first number?: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    while True:
        print("Available operations: ", " ".join(operations))
        operation = input("Pick an operation: ")
        if operation not in operations:
            print("Invalid operation. Please select a valid operation.")
            continue

        try:
            second_number = float(input("What is the second number?: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        result = calculator(first_number, operation, second_number)
        if result is not None:
            print(f"{first_number} {operation} {second_number} = {result}")
        else:
            print("Error in calculation. Please try again.")

        calc = input(
            "Type 'y' to continue calculating with the current result, "
            "'n' to start a new calculation, or 'exit' to quit: ").lower()
        if calc == "y":
            first_number = result
        elif calc == "n":
            break
        elif calc == "exit":
            print("Exiting the calculator.")
            exit()
        else:
            print("Invalid input. Exiting the calculator.")
            exit()
