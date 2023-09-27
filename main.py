#randome use for game logic selecting target and placing ships
import random
ranint = random.randint(0,10)
print(ranint)

rows = 10
cols = 10

lst = [["~"]*cols]*rows

#making the board
board = [["~" for i in range(cols)]for j in range(rows)]

print("   0    1    2    3    4    5    6    7    8    9")
for i in range (0,10):
    print(i, lst[i])

#This asks for the inputs on there P1 wants their first boats to go
# only odd boats total 6 ----  three 3s -- two 5s -- one 7
xinput = int(input("give me x "))
yinput = int(input("give me y "))
axis = input("L/R or U/D")
print("you picked"+ axis)


#this function using a random generator generates the location for the game logics first three boat
def game_logic_3boat():
    ran_dir = random.randint(0, 1)
    xinput = random.randint(1, 10)
    yinput = random.randint(1, 10)

    if ran_dir ==1:
        if board[xinput][yinput] == "~" and board[xinput + 1][yinput] == "~" and board[xinput-1][yinput] == "~":
            board[xinput][yinput] = "B"
            board[xinput + 1][yinput] = "B"
            board[xinput - 1][yinput] = "B"
    else:
        if board[xinput][yinput] == "~" and board[xinput][yinput + 1] == "~" and board[xinput][yinput - 1] == "~":
            board[xinput][yinput] = "B"
            board[xinput + 1][yinput] = "B"
            board[xinput - 1][yinput] = "B"
game_logic_3boat()


#this function places a three square long boat on the board as well as rotates it in the way that the player chooses
def three_boat ():
    if axis == "U" or  axis == "D" or axis == "U/D" or axis == "u" or axis == "d" or axis == "u/d":
        board[xinput][yinput] = "B"
        board[xinput + 1][yinput] = "B"
        board[xinput - 1][yinput] = "B"
    else:
        board[xinput][yinput] = "B"
        board[xinput + 1][yinput] = "B"
        board[xinput - 1][yinput] = "B"

three_boat()

#this reprints the board
for i in range(0,10):
    print(i, board[i])


#this function prompts the player to shoot their missles then runs a hit check and will tell the player if its a hit or a miss.
def pick_target():
    targetx = int(input("pick X coordinate to fire at"))
    targety = int(input("pick Y coordinate to fire at"))
    if board[targetx][targety] == "B":
        print("You hit my battleship!")
        board[targetx][targety] = "X"
    elif board[targetx][targety] == "X" or board[targetx][targety] == "O":
        print("You already shot here! You loose a turn")
    else:
        board [targetx][targety] = "O"
    for i in range(0, 10):
        print(i, lst[i])
pick_target()
three_boat()