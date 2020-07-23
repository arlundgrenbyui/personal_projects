from random import seed
from random import randint


class Sheet:
    """
    A simple implementation of a D&D-like character sheet. User inputs name,
    race, background, and class. Then the user is prompted to roll and assign
    their stats.
    """
    def __init__(self):
        name = input("What would you like your character's name to be? ")
        race = input("What race would you like your character to be? ")
        background = input("What background does your character have? ")
        c = input("What class is your character? ")
        self.char_info = Info(name, race, background, c, 1)
        self.stats = Stats(self.roll_stats())

    def get_modifier(self, contest):
        if int(self.stats.stat_book[contest]) >= 17:
            return 4
        elif int(self.stats.stat_book[contest]) >= 15:
            return 3
        elif int(self.stats.stat_book[contest]) >= 13:
            return 2
        elif int(self.stats.stat_book[contest]) >= 11:
            return 1
        elif int(self.stats.stat_book[contest]) >= 9:
            return 0
        elif int(self.stats.stat_book[contest]) >= 7:
            return -1
        elif int(self.stats.stat_book[contest]) >= 5:
            return -2
        elif int(self.stats.stat_book[contest]) >= 3:
            return -3

    def roll_4d6(self):
        a = randint(1, 6)
        b = randint(1, 6)
        c = randint(1, 6)
        d = randint(1, 6)
        return a + b + c + d - min(a, b, c, d)

    def roll_stats(self):
        print("Time to roll stats!")
        rolling = True
        seed(1)
        stat_book = {"STR": "?",
                     "DEX": "?",
                     "CON": "?",
                     "INT": "?",
                     "WIS": "?",
                     "CHA": "?"}
        statblock = None
        while rolling:
            a = self.roll_4d6()
            b = self.roll_4d6()
            c = self.roll_4d6()
            d = self.roll_4d6()
            e = self.roll_4d6()
            f = self.roll_4d6()
            response = input("You rolled: " + str(a) + " " + str(b) + " " + str(c)
                             + " " + str(d) + " " + str(e) + " " + str(f) + ". Would you like to keep these? Y/N ")
            if response == "Y":
                rolling = False
                statblock = [a, b, c, d, e, f]

        for stat in statblock:
            deciding = True
            while deciding:
                deciding = False
                response = input(
                    "What stat would you like to assign " + str(stat) + "? (STR, DEX, CON, INT, WIS, CHA) ")
                if response in stat_book and stat_book[response] == "?":
                    stat_book[response] = stat
                else:
                    deciding = True
                    print("Not valid (either a stat was already assigned, or a non-stat was selected ")

        print("These are your stats: ")
        for key, value in stat_book.items():
            print(key, value)
        return stat_book


class Info:
    """
    Holds the character's basic information.
    """
    def __init__(self, name, race, background, c, level):
        self.name = name
        self.race = race
        self.background = background
        self.c = c
        self.level = level


class Stats:
    """
    Maintains the character's stats.
    """
    def __init__(self, stat_book):
        self.stat_book = stat_book
        print("Statbook successfully added.")


sheet = Sheet()
print("Time to try some rolls, DC 15. ")
print("STR check: ")
roll = randint(1, 20)
print("You rolled: " + str(roll) + ", your modifier is " + str(sheet.get_modifier("STR")))
if roll + sheet.get_modifier("STR") >= 15:
    print("Pass!")
else:
    print("Fail!")

print("DEX check: ")
roll = randint(1, 20)
print("You rolled: " + str(roll) + ", your modifier is " + str(sheet.get_modifier("DEX")))
if roll + sheet.get_modifier("DEX") >= 15:
    print("Pass!")
else:
    print("Fail!")

print("INT check: ")
roll = randint(1, 20)
print("You rolled: " + str(roll) + ", your modifier is " + str(sheet.get_modifier("INT")))
if roll + sheet.get_modifier("INT") >= 15:
    print("Pass!")
else:
    print("Fail!")
