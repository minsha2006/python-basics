password = "abc12345"

has_letter = False
has_number = False

if len(password) >= 8:
    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_number = True

if len(password) >= 8 and has_letter and has_number:
    print("Valid password")
else:
    print("Invalid password")

