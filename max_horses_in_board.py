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
                place_horse(new_board, i, j)
                boards.append(new_board)

    return boards

def place_horse(board, i, j):
    board[i][j] = 1

# Returns a copy of the given board
def copy_board(board):
    return np.copy(board)

# Checks if the given position is valid to place a new horse on the given board
def is_valid_position(board, i, j):
    rows, columns = np.shape(board)

    if rows > i >= 0 and columns > j >= 0:  # If the given position is within the board limits
        if is_endangered_position(board, i, j):
            return False

        if board[i][j] == 1:
            return False

    return True


def is_endangered_position(board, i, j):
    rows, columns = np.shape(board)

    for dx, dy in HORSE_MOVES:
        di, dj = i + dx, j + dy  # Calculates the possible moves for a horse from the given position
        if 0 <= di < rows and 0 <= dj < columns and board[di][
            dj] == 1:  # If there is a horse on the calculated position
            return True

    return False

# Calculates the cost from the initial state to the current one on the given path
def cost_function(path):
    cost = 0
    current_state = path[0]
    initial_state = path[-1]
    initial_endangered_positions = 0
    current_endangered_positions = 0
    rows, columns = np.shape(current_state)

    for i in range(rows):
        for j in range(columns):
            if is_endangered_position(current_state, i, j):
                current_endangered_positions += 1
            if is_endangered_position(initial_state, i, j):
                initial_endangered_positions += 1

    cost = abs(current_endangered_positions - initial_endangered_positions)

    return cost

# Calculates the heuristic for the given state returning
# how many more horses are needed to reach the solution
def heuristic_function(board):
    placed_horses = 0
    rows, columns = np.shape(board)

    for i in range(rows):
        for j in range(columns):
            if board[i][j] == 1:
                placed_horses += 1

    heuristic = get_max_horse_number(board) - placed_horses
    return heuristic


def count_horses(board):
    rows, columns = np.shape(board)
    placed_horses = 0

    # Counts how many horses are in the board
    for i in range(rows):
        for j in range(columns):
            if board[i][j] == 1:
                placed_horses += 1

    return placed_horses

# Determines if a given board is the final solution
def is_solution(board):
    rows, columns = np.shape(board)

    for i in range(rows):
        for j in range(columns):
            if is_valid_position(board, i, j):
                return False

    return True

# Returns the max possible number of horses for the given configuration
def get_max_horse_number(board):
    M, N = np.shape(board)
    max_number = max(M,N)

    if M >= 3 and N >= 3:
        if (M*N) % 2 == 0:
            return int(M*N/2)
        else:
            return int(M*N/2) + 1
    elif M == N or M == 0 or N == 0:
        return M*N
    elif M == 1 or N == 1:
        return max_number
    else:
        if max_number % 4 == 0:
            return max_number
        elif max_number % 2 == 0:
            return max_number + 2
        else:
            return max_number + 1

# Checks if two boards are the same
def equal_boards(board1, board2):
    rows, columns = np.shape(board1)

    for i in range(rows):
        for j in range(columns):
            if board1[i][j] != board2[i][j]:
                return False

    return True

