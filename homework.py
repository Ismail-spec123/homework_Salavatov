maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]
win_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def prmaps():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])

def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol


def get_result():
    win = ""

    for i in win_lines:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"
    for f in maps:
        if (maps[0] == "X" or maps[0] == 'O') \
            and (maps[1] == "X" or maps[1] == 'O') \
            and (maps[2] == "X" or maps[2] == 'O') \
            and (maps[3] == "X" or maps[3] == 'O') \
            and (maps[4] == "X" or maps[4] == 'O') \
            and (maps[5] == "X" or maps[5] == 'O') \
            and (maps[6] == "X" or maps[6] == 'O') \
            and (maps[7] == "X" or maps[7] == 'O') \
            and (maps[8] == "X" or maps[8] == 'O'):
            win = 'ничья'

    return win


game_over = False
player1 = True

while game_over == False:

    prmaps()

    if player1 == True:
        symbol = "X"
        step = int(input("plaer 1 your turne: "))
    else:
        symbol = "O"
        step = int(input("plaer 2, your turne: "))

    step_maps(step, symbol)
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)


prmaps()
print("Победил", win)