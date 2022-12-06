import random
numbers = []
for i in range(1, 100):
    numbers.append(i)
#print(numbers)

def binary_search():
    personalGuess = int(input("Enter your guess: "))
    highGuess = 101
    lowGuess = 0
    numGuesses = 0
    while numGuesses != 7:
        guess = random.choice(numbers)
        print("\nGuess Number: " + str(numGuesses))
        print("Reminder: Your number is: ", personalGuess)
        print("I guessed:", guess)
        input1 = input("Was the guess high, low, or correct? ")
        if input1 == "high":
            highGuess = guess
            numbers.clear()
            for i in range(lowGuess + 1, highGuess):
                numbers.append(i)
            #print(numbers)
            #print("Low guess:", lowGuess, "High guess", highGuess)
            numGuesses += 1

        elif input1 == "low":
            lowGuess = guess
            numbers.clear()
            for i in range(lowGuess + 1, highGuess):
                numbers.append(i)
            #print(numbers)
            #print("Low guess:", lowGuess, "High guess", highGuess)
            numGuesses += 1

        elif input1 == "correct":
            print("I guessed correctly!")
            exit()

        else:
            print("Please enter a valid response.")

binary_search()