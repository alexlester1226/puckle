import random

selectedPlayer = ""
data = []
dataName = []
table = {'Name': [], 'Team': [], 'Position': [], 'Age': [], 'Hand': [], 'Height': [], 'Weight': [], 'Nationality': []}
init = False
colours = ["", "<span style='color: green;'>", "<span style='color: orange;'>", "</span>"]
teams = [["TOR", "MTL", "BUF", "OTT", "FLA", "BOS", "DET", "TBL"], ["CAR", "CBJ", "NJD", "NYI", "NYR", "PHI", "PIT", "WSH"],
         ["ANA", "CGY", "EDM", "LAK", "SJS", "VAN", "VGK", "SEA"], ["ARI", "CHI", "COL", "DAL", "MIN", "NSH", "STL", "WPJ"]]
display = "| Name | Team | Position | Age | Hand | Height | Weight | Nationality |\n| --- | --- | --- | --- | --- | --- | --- | --- |\n"
win = False

class Player:
    def __init__(self, name, pos, age, nationality, height, weight, hand, team):
        strName = ''
        for i in range(0, len(name)):
            if name[i] == '\xa0':
                break
            else:
                strName += name[i]
        self.name = strName
        self.pos = pos
        self.age = age
        self.nationality = nationality
        self.height = height
        self.weight = weight
        self.hand = hand
        self.team = team
        data.append(self)
        dataName.append(self.name)


def update(player):
    global table
    table['Name'].append(player.name)
    table['Position'].append(player.pos)
    table['Age'].append(player.age)
    table['Hand'].append(player.hand)
    table['Height'].append(player.height)
    table['Weight'].append(player.weight)
    table['Nationality'].append(player.nationality)
    table['Team'].append(player.team)


def resetTable():
    global table, display, win
    table = {'Name': [], 'Team': [], 'Position': [], 'Age': [], 'Hand': [], 'Height': [], 'Weight': [], 'Nationality': []}
    display = "| Name | Team | Position | Age | Hand | Height | Weight | Nationality |\n| --- | --- | --- | --- | --- | --- | --- | --- |\n"
    selectPlayer()
    win = False

def read():
    f = open('database.txt', 'r')
    line = f.readlines()
    f.close()
    for i in range(0, len(line)):
        # name, pos, age, nationality, height, weight, hand
        info = line[i].split(',')
        p = Player(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7])


def selectPlayer():
    global selectedPlayer
    x = random.randint(0, len(data))
    selectedPlayer = data[x]


def checkGuess(index):
    global display
    guess = data[index]

    result = []
    if guess.name == selectedPlayer.name:
        result.append(1)
    else:
        result.append(0)

    div = 5
    for i in range(0, 4):
        if selectedPlayer.team in teams[i]:
            div = i


    if guess.team == selectedPlayer.team:
        result.append(1)
    elif guess.team in teams[div]:
        result.append(2)
    else:
        result.append(0)

    if guess.pos == selectedPlayer.pos:
        result.append(1)
    else:
        result.append(0)

    if guess.age == selectedPlayer.age:
        result.append(1)
    elif abs(int(guess.age)-int(selectedPlayer.age)) <= 2:
        result.append(2)
    else:
        result.append(0)

    if guess.hand == selectedPlayer.hand:
        result.append(1)
    else:
        result.append(0)

    if guess.height == selectedPlayer.height:
        result.append(1)
    elif guess.height[0] == selectedPlayer.height[0]:
        result.append(2)
    else:
        result.append(0)

    if guess.weight == selectedPlayer.weight:
        result.append(1)
    elif abs(int(guess.weight)-int(selectedPlayer.weight)) <= 15:
        result.append(2)
    else:
        result.append(0)

    if guess.nationality == selectedPlayer.nationality:
            result.append(1)
    else:
        result.append(0)

    # 0 = nothing, 1 = green, 2 = yellow
    #  name, pos, age, nationality, height, weight, hand, team):
    # {'Name': [], 'Team': [], 'Position': [], 'Age': [], 'Hand': [], 'Height': [], 'Weight': [], 'Nationality': []}
    # colours = ["", "<span style='color: green;'>", "<span style='color: yellow;'>", "</span>"]
    display += f"| {colours[result[0]]}{guess.name}{colours[3]} | {colours[result[1]]}{guess.team}{colours[3]} | {colours[result[2]]}{guess.pos}{colours[3]} | {colours[result[3]]}{guess.age}{colours[3]} | {colours[result[4]]}{guess.hand}{colours[3]} | {colours[result[5]]}{guess.height}{colours[3]} | {colours[result[6]]}{guess.weight}{colours[3]} | {colours[result[7]]}{guess.nationality}{colours[3]} |\n"

