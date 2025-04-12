"""Modules -- bonus experiment day 14. We right clicked on the functions and moved the functions
by clicking on move and refactor. Below are the import statements."""
from converter14 import convert
from parse14 import parse

feet_inches = input("Enter feet and inches: ")

f, i = parse(feet_inches)
print('fi: ', f, i)

result = convert(f, i)

if result < 1:
    print("The kid cannot use the slide.")
else:
    print("Hooray.. the kid can use the slide!!!")