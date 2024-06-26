import calculator_ascii

print(calculator_ascii.art)


def calculator(first_number, operation, second_number):
    if operation is "+":
        result = first_number + second_number
        return result
    if operation is "-":
        result = first_number - second_number
        return result
    if operation is "*":
        result = first_number * second_number
        return result
    if operation is "/":
        result = first_number / second_number
        return result


new_calc = True
operations = ["+", "-", "*", "/"]

while new_calc is True:
    first_number = float(input("What is the first number?: "))
    continue_calc = True

    for operation in operations:
        print(operation)

    while continue_calc is True:
        operation = input("Pick an operation: ")
        second_number = float(input("What is the second number?: "))
        result = calculator(first_number, operation, second_number)
        print(f"{first_number} {operation} {second_number} = {result}")
        calc = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to "
            f"start a new calculation: ")
        if calc == "y":
            new_calc = False
            first_number = result
        if calc == "n":
            new_calc = True
            continue_calc = False

