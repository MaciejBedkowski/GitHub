import random

number = []
dies_attacker = 0
dies_defender = 0


def roll():
    for x in range(5):
        number.append(random.randint(1, 6))
    return number


def print_attacker(index):
    print("Attacker:" + str(number[0]) +"-" + str(number[1]) + "-" + str(number[2]))


def print_defender(index):
    print("Defender:" + str(number[3]) + "-" + str(number[4]))


def reroll():
    number = []
    for x in range(5):
        number.append(random.randint(1, 6))
    return number


def count_attacker(index):
    attacker = 0
    for x in range(3):
        attacker += number[x]
    return attacker


def count_defender(index):
    defender = 0
    for x in range(4, 2, -1):
        defender += number[x]
    return defender


while True:
    print("|||| MENU ||||")
    print("0. Wyjscie")
    print("1. Wylosuj")
    choice = int(input("Podaj swój wybór: "))
    if choice == 0:
        break
    elif choice == 1:
        number = roll()
        print_attacker(number)
        print_defender(number)
        attacker = count_attacker(number)
        defender = count_defender(number)
        if defender > attacker:
            dies_attacker += 1
        elif defender == attacker:
            dies_attacker += 1
        else:
            dies_defender += 1
        number = reroll()
        print("Śmierci atakującego:" + str(dies_attacker) + ", Śmierci broniącego:" + str(dies_defender))
    else:
        print("**** Podałeś nieprawidłową opcję ****")