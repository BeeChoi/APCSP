toConvert = float(input("How much money do you have? $"))

print("""
Choices:
1: Euros
2: Canadian Dollar
3: Indian Rupee
4: Japanese Yen
5: Vietnamese Dong
6: Korean Won
7: Bitcoin (Fake Money)
""")
validInputs = ["1", "2", "3", "4", "5", "6", "7"]
currency = input("What currency do you want to convert to? ")
while currency not in validInputs:
    print("Error | Not a valid currency.")
    currency = input("What currency do you want to convert to? ")

if currency == "1":
    print(f"{toConvert * 0.81} Euros")
elif currency == "2":
    print(f"{toConvert * 1.29} Canadian Dollars")
elif currency == "3":
    print(f"{toConvert * 83.03} Indian Rupee")
elif currency == "4":
    print(f"{toConvert * 110.49} Japanese Yen")
elif currency == "5":
    print(f"{toConvert * 22750} Vietnamese Dong")
elif currency == "6":
    print(f"{toConvert * 1079.43} Korean Won")
elif currency == "7":
    print(f"{toConvert * 0.000088} Bitcoin")
else:
    print("Invalid currency") 