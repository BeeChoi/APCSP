import random
birthdays = []
for y in range(10):
    birthdays.append(str(random.randint(1, 12)) + "/" + str(random.randint(1, 31)))
    y += 1
print(birthdays)

def selection_sort():
    newBirthdays = []
    for i in range(len(birthdays)):
        newBirthdays.append(min(birthdays))
        birthdays.remove(min(birthdays))
    return newBirthdays

def bubble_sort():
    for i in range(len(birthdays)):
        for j in range(len(birthdays) - 1):
            if birthdays[j] > birthdays[j + 1]:
                birthdays[j], birthdays[j + 1] = birthdays[j + 1], birthdays[j]
    return birthdays

print(selection_sort())
print("----------------")
print(bubble_sort())