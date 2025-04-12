"""Check the password.
1) Must have atlease 8 characters.
2) A number
3) Atleast 1 capital letter"""

password = input("Enter your password: ")
result = {}

# Check length
result["Length"] = len(password) >= 8

# Check for at least one digit
result["Digits"] = any(char.isdigit() for char in password)

# Check for at least one uppercase letter
result["Upper-Case"] = any(char.isupper() for char in password)

print(result)  # Print the result dictionary after all checks

# Check if all conditions are met
if all(result.values()):
    print("Strong Password!")
else:
    print("Weak Password.")


"""password = input("Enter your password: ")
result = {}

if len(password) >= 8:
    result["Length"] = True
else:
    result["Length"] = False
print(result)

digit = False
for i in password:
    if i.isdigit():
        digit = True
result["Digits"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result["Upper-Case"] = uppercase

if all(result.values()):
    print("Strong Password!")
else:
    print("Weak Password.")"""