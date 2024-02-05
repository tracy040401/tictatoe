"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_X = sum(row.count('X') for row in board)
    count_O = sum(row.count('O') for row in board)

    if(count_X > count_O):
        return 'O'
    else:
        return 'X'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if(board[i][j] == EMPTY):
                possible_actions.add((i,j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        return board
    new_board = [row[:] for row in board]
    if(player(board) == X):
        new_board[action[0]][action[1]] = X
    else:
        new_board[action[0]][action[1]] = O
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    for i in range(3):
        if(board[i][0] == board[i][1] == board[i][2] != EMPTY):
            return board[i][0]
        elif(board[0][i] == board[1][i] == board[2][i] != EMPTY):
            return board[0][i]

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    elif all(cell != EMPTY for row in board for cell in row):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(winner(board)==X):
        return 1
    elif(winner(board)==O):
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(terminal(board)):
        return None
    curr_player = player(board)

    if curr_player == X:
        best_score = -math.inf
        best_move = None
        for action in actions(board):
            score = min_value(result(board, action))
            if score > best_score:
                best_score = score
                best_move = action
    else:
        best_score = math.inf
        best_move = None
        for action in actions(board):
            score = max_value(result(board, action))
            if score < best_score:
                best_score = score
                best_move = action
    return best_move

def max_value(board):
    if(terminal(board)):
        return utility(board)
    res = -math.inf
    for action in actions(board):
        res = max(res, min_value(result(board, action)))
    return res

def min_value(board):
    if(terminal(board)):
        return utility(board)
    res = math.inf
    for action in actions(board):
        res = min(res, max_value(result(board, action)))
    return res