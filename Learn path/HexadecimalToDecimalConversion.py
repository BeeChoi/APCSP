type = input("Is your number in decimal or hexadecimal? ")
if type == "decimal":
    num = int(input("What number would you like to convert? "))
    hex = hex(num)
    print(hex)
    print("*Note: 0x denotes that the number is in hexadecimal.")
elif type == "hexadecimal":
    num = input("What number would you like to convert? ")
    dec = int(num, 16)
    print(dec)