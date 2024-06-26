# Functions with outputs
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"


print(format_name("aurimas", "AURIMAS"))


# Multiple returns

def format_name_second(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didnt provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"


print(format_name_second(input("What is your first name?"), input("What is "
                                                                  "your last name?")))
