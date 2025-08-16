"""
Tic Tac Toe Player
"""

import math
import copy

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
    count = sum(1 for raw in board for val in raw if val != EMPTY)
    return X if count % 2 == 0 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in [0, 1, 2] for j in [0, 1, 2] if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")
    
    resulting_board = copy.deepcopy(board)
    resulting_board[action[0]][action[1]] = player(board)
    return resulting_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if terminal(board):
        u = utility(board)
        return X if u == 1 else O if u == -1 else None

    return winner(result(board, minimax(board)))


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if board[0][0] != EMPTY and board[0][0] == board[1][1] == board[2][2]:
        return True
    
    if board[0][2] != EMPTY and board[0][2] == board[1][1] == board[2][0]:
        return True
    
    for row in board:
        if row[0] != EMPTY and row[0] == row[1] == row[2]:
            return True
    
    for c in [0, 1, 2]:
        if board[0][c] != EMPTY and board[0][c] == board[1][c] == board[2][c]:
            return True
    
    if sum(1 for raw in board for val in raw if val != EMPTY) == 9:
        return True
    
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if board[0][0] == board[1][1] == board[2][2] == X or board[0][2] == board[1][1] == board[2][0] == X:
        return 1
    
    if board[0][0] == board[1][1] == board[2][2] == O or board[0][2] == board[1][1] == board[2][0] == O:
        return -1
    
    for row in board:
        if row[0] == row[1] == row[2] == X:
            return 1
        if row[0] == row[1] == row[2] == O:
            return -1
    
    for c in [0, 1, 2]:
        if board[0][c] == board[1][c] == board[2][c] == X:
            return 1
        if board[0][c] == board[1][c] == board[2][c] == O:
            return -1
    
    if sum(1 for raw in board for val in raw if val != EMPTY) == 9:
        return 0


def max_value(board):
    v = -math.inf

    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v


def min_value(board):
    v = math.inf

    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        return max(actions(board), key=lambda action: min_value(result(board, action)))
    else:
        return min(actions(board), key=lambda action: max_value(result(board, action)))