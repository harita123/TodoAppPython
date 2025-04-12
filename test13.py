"""Getting age"""
def get_age(year_of_birth, current_year=2025):
    return current_year - year_of_birth

age = get_age(1981)
print(age)

"""using split function"""

def get_nr_items(user_input):
    items = user_input.split(",")
    cleaned_items = [item.strip() for item in items if item.strip()]
    return len(cleaned_items)

result_nr_items = get_nr_items("john,lisa,teresa")
print(result_nr_items)


"""Area of square"""


def square_area(length):
    area_of_square = length * length
    return area_of_square


result_area_of_square = square_area(4)
print(result_area_of_square)

"""Temperature checker"""
def temp_checker(temp):
    if temp > 7:
        return("Warm")
    else:
        return("Cold")

result_temp_check = temp_checker(9)
print(result_temp_check)

"""Checking if password length is greater than 8"""


def pass_strength(password):
    if len(password) < 8:
        return False
    else:
        return True


result_pass_strength = pass_strength("password")
print(result_pass_strength)