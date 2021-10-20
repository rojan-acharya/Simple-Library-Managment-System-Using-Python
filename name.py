def validateName(username):
    if username.isalpha():
        return username
    else:
        print("Please enter a proper name!")
        return getName()

def getName():
    firstName = validateName(input("Enter your first name: "))
    lastName = validateName(input("Enter your last name: "))
    fullName = firstName + (" ") + lastName
    return fullName