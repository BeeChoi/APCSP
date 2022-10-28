
def triangle():
    side1 = float(input("What is the first side of the triangle? "))
    side2 = float(input("What is the second side of the triangle? "))
    side3 = float(input("What is the third side of the triangle? "))
    perimeter = side1 + side2 + side3
    print(f"The perimeter of the triangle is {perimeter}")

def circle():
    radius = float(input("What is the radius of the circle? "))
    perimeter = 2 * 3.14 * radius
    print(f"The perimeter of the circle is {perimeter}")

def square():
    side = float(input("What is the length of the side of the square? "))
    perimeter = side * 4
    print(f"The perimeter of the square is {perimeter}")

def rectangle():
    length = float(input("What is the length of the rectangle? "))
    width = float(input("What is the width of the rectangle? "))
    perimeter = (length + width) * 2
    print(f"The perimeter of the rectangle is {perimeter}")

def parallelogram():
    base = float(input("What is the base of the parallelogram? "))
    side = float(input("What is the side of the parallelogram? "))
    perimeter = (base + side) * 2
    print(f"The perimeter of the parallelogram is {perimeter}")

def trapezoid():
    base1 = float(input("What is the first base of the trapezoid? "))
    base2 = float(input("What is the second base of the trapezoid? "))
    side1 = float(input("What is the first side of the trapezoid? "))
    side2 = float(input("What is the second side of the trapezoid? "))
    perimeter = base1 + base2 + side1 + side2
    print(f"The perimeter of the trapezoid is {perimeter}")

shape = input("what shape would you like to calculate the perimeter of? ")
if shape == "triangle":
    triangle()
elif shape == "circle":
    circle()
elif shape == "square":
    square()
elif shape == "rectangle":
    rectangle()
elif shape == "parallelogram":
    parallelogram()
elif shape == "trapezoid":
    trapezoid()
else:
    print("Error: Invalid Shape")
    exit()
    