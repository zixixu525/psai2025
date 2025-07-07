def create_board():
    board=[]
    for i in range(3):
        for j in range(3):
            board.append('#')
    return board

def print_board(board):
    for i in range(3):
        print("---------")
        print(" | ".join(board[0:3]))


print_board(create_board())
            