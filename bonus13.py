"""Converting feet and inches into meters"""

feet_inches = input("Enter feet and inches: ")

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches

def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    print(f'{feet} feet and {inches} inches is {meters}')
    return meters

f, i = parse(feet_inches)
print('fi: ', f, i)

result = convert(f, i)

if result < 1:
    print("The kid cannot use the slide.")
else:
    print("Hooray.. the kid can use the slide!!!")