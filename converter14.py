def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    print(f'{feet} feet and {inches} inches is {meters}')
    return meters
