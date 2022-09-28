symbols = "!@#$%^&*()_+-=<>?/.,;:[]{}|"
uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercaseLetters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
alnumCount = 0
symbolCount = 0
numberCount = 0

password = input("Enter a crusty password: ")

if " " in password:
    print("No spaces allowed.")
    exit()
elif len(password) < 8:
    print("Password must be at least 8 characters.")
    exit()
else:
    for char in password:
        if char in symbols:
            symbolCount += 1
        elif char in uppercaseLetters:
            alnumCount += 1
        elif char in lowercaseLetters:
            alnumCount += 1
        elif char in numbers:
            numberCount += 1
    if len(password) < 10 and symbolCount == 0 and numberCount == 0:
        print("Very Weak")
    elif len(password) > 10 and (symbolCount == 0 and numberCount > 0) or (symbolCount > 0 and numberCount == 0):
        print("Weak")
    elif len(password) > 12 and symbolCount > 2 and numberCount > 2:
        print("Strong")
    elif len(password) > 16 and symbolCount > 5 and numberCount > 5:
        print("Very Strong")
    else:
        print("Weak")
    