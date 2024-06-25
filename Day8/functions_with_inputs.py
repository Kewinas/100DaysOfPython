def greet():
    print("Hello")
    print("How do you do?")
    print("Isnt the weather nice today?")


greet()


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print("Isnt the weather nice today?")


greet_with_name("Aurimas")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Aurimas", "Vilnius")

greet_with(name = "Aurimas", location = "Vilnius")


