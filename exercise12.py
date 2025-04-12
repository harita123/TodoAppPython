def strength(password):
    if len(password) >= 8:
        has_upper = False
        has_digit = False
        for char in password:
            if char.isupper():
                has_upper = True

            elif char.isdigit():
                has_digit = True
        if has_upper and has_digit:
            return "Strong Password"
        else:
            return "Weak Password"
    else:
        return "Weak Password"

print(strength("Password1"))