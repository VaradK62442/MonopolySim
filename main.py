from random import randint 
import matplotlib.pyplot as plt

class space:
    def __init__(self, name, timesLanded=0):
        self.n = name
        self.t = timesLanded

def makeBoard():
    board = ['Go', 'Old Kent Road', 'Community Chest 1', 'Whitechapel Road', 'Income Tax', 'Kings Cross Station', 'The Angel Islington', 'Chance 1', 'Euston Road', 'Pentonville Road',
            'Jail / Just Visiting', 'Pall Mall', 'Electric Company', 'Whitehall', 'Northumberland Avenue', 'Marylebone Station', 'Bow Street', 'Community Chest 2', 'Marlborough Street',
            'Vine Street', 'Free Parking', 'Strand', 'Chance 2', 'Fleet Street', 'Trafalgar Square', 'Fenchurch St. Station', 'Leicester Square', 'Coventry Street', 'Water Works',
            'Piccadilly', 'Go To Jail', 'Regent Street', 'Oxford Street', 'Community Chest 3', 'Bond Street', 'Liverpool St. Station', 'Chance 3', 'Park Lane', 'Super Tax', 'Mayfair']

    spaces = []
    for i in range(len(board)):
        spaces.append('space')
        spaces[-1] = space(board[i])

    spaces[0].t = 1

    return spaces

def rollDice():
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    return dice1 + dice2, dice1, dice2

def main():
    spaces = makeBoard()
    rolls = []
    currPos = 0
    for i in range(10000000):
        vals = rollDice()
        rolls.append(vals)

        #print(f"Dice rolled: {vals[1]} and {vals[2]}")

        currPos += vals[0]
        while currPos > 39:
            currPos -= 40
        spaces[currPos].t += 1
        # going to jail methods
        # landing on go to jail
        if currPos == 30:
            currPos = 10
            spaces[currPos].t += 1
        # picking up comm chest or chance
        if currPos in [2, 17, 33, 7, 22, 36]:
            if randint(1, 16) == 1:
                currPos = 10
                spaces[currPos].t += 1
        # rolling three doubles
        if len(rolls) >= 3:
            doubleCount = 0
            i = 0

            if rolls[-1][1] == rolls[-1][2] and rolls[-2][1] == rolls[-2][2] and rolls[-3][1] == rolls[-3][2]:
                #print(rolls[-1][1], rolls[-1][2], rolls[-2][1], rolls[-2][2], rolls[-3][1], rolls[-3][2])
                currPos = 10
                spaces[currPos].t += 1  

        #print(f"Position: {spaces[currPos].n}")              

    spaces.sort(key=lambda x: x.t)

    for j in range(len(spaces)):
        print(f"Name: {spaces[j].n}\nTimes Landed On: {spaces[j].t}\n")

    plt.scatter([spaces[i].n for i in range(len(spaces))], [spaces[i].t for i in range(len(spaces))])
    plt.xticks(rotation='vertical')
    plt.show()

if __name__ == "__main__":
    main()