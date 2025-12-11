import math

human = "O"
ai = "X"

board = [" " for _ in range(9)]

def print_board(b):
    for i in range(3):
        print(b[3*i], "|", b[3*i+1], "|", b[3*i+2])
        if i < 2:
            print("---------")

def empty_cells(b):
    return [i for i in range(9) if b[i] == " "]

def winner(b, player):
    win_states = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(b[a] == b[b_] == b[c] == player for a,b_,c in win_states)

def game_over(b):
    return winner(b, human) or winner(b, ai) or len(empty_cells(b)) == 0

def minimax(b, depth, is_max):
    if winner(b, ai):
        return 1
    if winner(b, human):
        return -1
    if len(empty_cells(b)) == 0:
        return 0

    if is_max:
        best = -math.inf
        for idx in empty_cells(b):
            b[idx] = ai
            score = minimax(b, depth + 1, False)
            b[idx] = " "
            best = max(best, score)
        return best
    else:
        best = math.inf
        for idx in empty_cells(b):
            b[idx] = human
            score = minimax(b, depth + 1, True)
            b[idx] = " "
            best = min(best, score)
        return best

def ai_move():
    best_score = -math.inf
    best_move = None
    for idx in empty_cells(board):
        board[idx] = ai
        score = minimax(board, 0, False)
        board[idx] = " "
        if score > best_score:
            best_score = score
            best_move = idx
    board[best_move] = ai

def human_move():
    while True:
        pos = int(input("enter position (1-9): ")) - 1
        if pos in empty_cells(board):
            board[pos] = human
            break
        else:
            print("invalid move babes, try again")

print("tic tac toe - you are O, ai is X")
print_board(board)

while not game_over(board):
    human_move()
    print_board(board)
    if game_over(board):
        break

    ai_move()
    print("ai move:")
    print_board(board)

if winner(board, ai):
    print("ai wins 😭")
elif winner(board, human):
    print("you win queen 🎀")
else:
    print("draw 💫")
