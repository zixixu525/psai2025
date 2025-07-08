import copy

def print_board(board):
    for row in board:
        print(' | '.join(row))
    print()

def check_winner(board):
    lines = (
        board[0], board[1], board[2],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    )
    for line in lines:
        if line[0] != ' ' and line.count(line[0]) == 3:
            return line[0]
    return None

def is_terminal(board):
    return check_winner(board) is not None or all(cell != ' ' for row in board for cell in row)

def utility_force_tie(board, player):
    winner = check_winner(board)
    if winner == player:
        return -100  # Penalize own win
    elif winner is not None:
        return -100  # Penalize opponent win too
    else:
        return +100  # Draw is best

def heuristic_force_tie(board, player):
    opponent = 'O' if player == 'X' else 'X'
    score = 0
    lines = (
        board[0], board[1], board[2],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    )
    for line in lines:
        if line.count(player) == 2 and line.count(' ') == 1:
            score -= 10  # Avoid setting up own win
        if line.count(opponent) == 2 and line.count(' ') == 1:
            score += 10  # Encourage blocking opponent
    return score

def get_legal_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append((i, j))
    return moves

def apply_move(board, move, player):
    new_board = copy.deepcopy(board)
    new_board[move[0]][move[1]] = player
    return new_board

def minimax_force_tie(board, depth, is_maximizing, cutoff_depth, player):
    if is_terminal(board):
        return utility_force_tie(board, player)
    if depth == cutoff_depth:
        return heuristic_force_tie(board, player)
    
    if is_maximizing:
        max_eval = float('-inf')
        for move in get_legal_moves(board):
            eval = minimax_force_tie(apply_move(board, move, player), depth + 1, False, cutoff_depth, player)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        opponent = 'O' if player == 'X' else 'X'
        for move in get_legal_moves(board):
            eval = minimax_force_tie(apply_move(board, move, opponent), depth + 1, True, cutoff_depth, player)
            min_eval = min(min_eval, eval)
        return min_eval

def best_move_force_tie(board, player, cutoff_depth):
    moves = get_legal_moves(board)
    best = None
    best_val = float('-inf')
    for move in moves:
        val = minimax_force_tie(apply_move(board, move, player), 1, False, cutoff_depth, player)
        if val > best_val:
            best_val = val
            best = move
    return best

# --------------------------
# DEMO GAME LOOP
# --------------------------
if __name__ == "__main__":
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    cutoff_depth = 3

    current_player = 'X'

    print("TIC TAC TOE - Forced Tie AI")
    print_board(board)

    while not is_terminal(board):
        if current_player == 'X':
            move = best_move_force_tie(board, 'X', cutoff_depth)
            print(f"AI (X) chooses: {move}")
        else:
            move = best_move_force_tie(board, 'O', cutoff_depth)
            print(f"AI (O) chooses: {move}")
        board = apply_move(board, move, current_player)
        print_board(board)
        current_player = 'O' if current_player == 'X' else 'X'

    winner = check_winner(board)
    if winner:
        print(f"Winner: {winner}")
    else:
        print("It's a draw!")
