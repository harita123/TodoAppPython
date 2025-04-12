"""Calculate the area of a rectangle. -- 1"""
"""Calculate the area of rectangle with try except block"""
"""Do not allow user to enter the save value for length and breath"""
try:
    width = float(input("Enter rectangle width: "))
    height = float(input("Enter rectangle height: "))
    if width == height:
        exit("That looks like a square.")
    area = width * height
    print(f'The area of the rectangle is : {area}')
except ValueError:
    print("Enter a number")
