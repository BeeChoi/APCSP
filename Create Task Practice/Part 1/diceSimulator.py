import random

def roll_dice(num_rolls, num_dice):
    sum = []
    if num_dice == 0:
        return []
    else:
        for i in range(num_rolls):
            tmp = 0
            for i in range(num_dice):
                tmp += random.randint(1, 6)
            sum.append(tmp)
        return sum

def mean(sumDice):
    return sum(sumDice) / len(sumDice)

def median(sumDice):
    sumDice.sort()
    if len(sumDice) % 2 == 0:
        return (sumDice[len(sumDice) // 2] + sumDice[len(sumDice) // 2 - 1]) / 2
    else:
        return sumDice[len(sumDice) // 2]


def mode(sumDice):
    return max(set(sumDice), key=sumDice.count)






def main():
    num_rolls = int(input("How many times do you want to roll the dice? "))
    num_dice = int(input("How many dice do you want to roll? "))
    sumDiceList = roll_dice(num_rolls, num_dice)
    print(sumDiceList)
    print(mean(sumDiceList))

main()