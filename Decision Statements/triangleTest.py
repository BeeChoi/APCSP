SideOne = input("What is the measurement of your first side? ")
SideTwo = input("What is the measurement of your second side? ")
SideThree = input("What is the measurement of your third side? ")

if SideOne.isalpha() or SideTwo.isalpha() or SideThree.isalpha():
    print("Error | Invalid measurement(s) given.")
    exit()
else:
    SideOne = float(SideOne)
    SideTwo = float(SideTwo)
    SideThree = float(SideThree)
    if (SideOne+SideTwo <= SideThree) or (SideOne+SideThree <= SideTwo) or (SideTwo+SideThree <= SideTwo):
        print("Not a triangle")

    elif (SideOne == SideTwo) and (SideTwo == SideThree):
        print("Equilateral Triangle")

    elif ((SideOne == SideTwo) and (SideTwo != SideThree)) or ((SideThree == SideTwo) and (SideTwo != SideOne)) or ((SideThree == SideOne) and (SideOne != SideTwo)):
        print("Isosceles Triangle")

    elif (SideOne != SideTwo and SideTwo != SideThree and SideThree !=  SideOne):
        print("Scalene Triangle")