import random as rd
from render_board import render
from adjacent import neighbours
import time,sys, subprocess

def random_state():
    alive_or_dead = ["  ","██"]
    probabilites = [0.8,0.2]

    states = rd.choices(alive_or_dead, weights = probabilites, k=1)
    return states[0]

def random_state(row : int, column: int):
    dead_board = [["  " for _ in range(column)] for _ in range(row)]
    for i in range(row):

        for j in range(column):
            dead_board[i][j] = random_state()
    return dead_board

"""
    Rules :
        - Any live cell with 0 or 1 live neighbours becomes dead, because of underpopulation
        - Any live cell with 2 or 3 live neighbours stays alive, because its neighborhood is just right
        - Any live cell with more than 3 live neighbours becomes dead, because of overpopulation
        - Any dead cell with exactly 3 live neighbours becomes alive, by reproduction
       = dead
    ██ = alive
"""

def next_board_state(board_state):
    rows = len(board_state)
    columns = len(board_state[0])
    new_board = [row[:] for row in board_state]
 
    # print("previous gen ______- ")
    # render(board_state)
    # print(board_state[x][y])
    # print(f"the element : {board_state[x][y]} at pos : [{x,y}] has the following neighbords (all 8 directions) : {(neighbord(board_state, 2,2))}")

    for i in range(rows):
        alive = "██"
        dead = "  "
        for j in range(columns):
            immediate_neighbours = neighbours(board_state, i , j)
            if board_state[i][j] == alive:
                if immediate_neighbours[alive] == 0 or immediate_neighbours[alive] == 1: #underpopulation
                    new_board[i][j] = dead
                elif immediate_neighbours[alive] == 2 or immediate_neighbours[alive] == 3: #just right
                    new_board[i][j]  = alive
                elif immediate_neighbours[alive] > 3: #overpopulation
                    new_board[i][j] = dead
            else:
                if immediate_neighbours[alive] ==3: #reproduction
                    new_board[i][j] = alive

    # print("new gen")
    # render(new_board)
    return new_board




print("Welcome to Life, the program will run up to 50 generations")
r, c = input("insert a row and column to initialize the board : ").split()
initial_board_state = random_state(int(r) ,int(c))
current_board = initial_board_state 



def clear():
    subprocess.run('clear' if sys.platform != 'win32' else 'cls', shell = True)
for i in range(50):
    
    clear()
    print(f"generation {i}")
    render(current_board)
    current_board = next_board_state(current_board)
    time.sleep(0.2)



print(f"initial state was : \n")
render(initial_board_state)
print(f"end state : \n")
render(current_board)