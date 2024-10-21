import numpy as np

HORSE_MOVES = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                (1, 2), (1, -2), (-1, 2), (-1, -2)]

# Returns a board of 0s with MxN dimensions
def initial_state(M, N):
    return [[0 for i in range(N)]for i in range(M)]

# Returns a list with the successors for the given state
def get_successors(board):
    rows, columns = np.shape(board)
    boards = []

    for i in range(rows):
        for j in range(columns):
            if is_valid_position(board, i, j):
                new_board = copy_board(board)
                new_board[i][j] = 1
                boards.append(new_board)

    return boards

# Returns a copy of the given board
def copy_board(board):
    return np.copy(board)

# Checks if the given position is valid to place a new horse on the given board
def is_valid_position(board, i, j):
    rows, columns = np.shape(board)

    if rows > i >= 0 and columns > j >= 0: # If the given position is within the board limits
        for dx, dy in HORSE_MOVES:
            di, dj = i + dx, j + dy # Calculates the possible moves for a horse from the given position
            if 0 <= di < rows and 0 <= dj < columns and board[di][dj] == 1: # If there is a horse on the calculated position
                return False

    return True

# Calculates the cost from the initial state to the current one on the given path
def cost_function(path):
    if len(path) == 0:
        return 0

    current_state = path[0]
    rows, columns = np.shape(current_state)

    invalid_positions = 0

    # Counts how many zeros there are in the board
    for i in range(rows):
        for j in range(columns):
            if not is_valid_position(current_state, i, j):
                invalid_positions += 1

    return current_nonplaced_horses

# Calculates the heuristic for the given state
def heuristic_function(board):
    pass

# Determines if a given board is the final solution
def is_solution(board):


    return True


