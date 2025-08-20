
def render(board_state:list):
    row = len(board_state)
    column = len(board_state[0])
    for i in range(row):
        for j in range(column):
            print(board_state[i][j], end = "")
        print("")


def join_new_board(board_state:list) -> str:
    return "\n".join("".join(row) for row in board_state)

