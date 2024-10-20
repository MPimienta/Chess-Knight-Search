import numpy as np
posible_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                       (1, 2), (1, -2), (-1, 2), (-1, -2)]

def initial_state(M, N):
    return [[0 for i in range(M)]for i in range(N)]

def get_next_states(board):
    rows, columns = np.shape(board)
    boards = []

    for i in range(rows):
        for j in range(columns):
            new_board = copy_board(board)
            place_horse(new_board, i, j)
            boards.append(new_board)

    return boards

def expand(path):
    path_expansion = get_next_states(path[0])

    new_paths = []
    for n in path_expansion:
        if not np.any(np.all(n == path, axis=(1, 2))):
            new_paths.append([n]+path)

    return new_paths

def copy_board(board):
    new_board = np.copy(board)
    return new_board

def place_horse(board, i, j):
    if is_valid_position(board, i, j):
        board[i][j] = 1

def is_valid_position(board, i, j):
    rows, columns = np.shape(board)
    if i >= 0 and i < rows and j >= 0 and j < columns:
        for dx, dy in posible_moves:
            di, dj = i + dx, j + dy
            if di >= 0 and di < rows and dj >= 0 and dj < columns and board[di][dj] == 1:
                return False

        if board[i][j] == 1:
            return False

        return True
    else:
        return False

def is_solution(board):
    horse_count = 0
    rows, columns = np.shape(board)

    for i in range(rows):
        for j in range(columns):
            if board[i][j] == 1:
                horse_count += 1

    max_horse_number = get_max_number(rows, columns)

    if horse_count == max_horse_number:
        return True
    else:
        return False

def get_max_number(M, N):
    if M < 3 <= N:
        return N
    elif M == N and M < 3:
        return M*N
    elif N < 3:
        return M
    else:
        if M*N % 2 == 0:
            return int((M * N)/2)
        else:
            return int((M*N) / 2 + 1)


def cost_function(path):
    if len(path) == 0:
        return 0

    initial_state = path[-1]
    final_state = path[0]
    rows, columns = np.shape(initial_state)

    initial_placed_horses = 0
    final_placed_horses = 0

    for i in range(rows):
        for j in range(columns):
            if initial_state[i][j] == 1:
                initial_placed_horses += 1
            if final_state[i][j] == 1:
                final_placed_horses += 1

    cost = final_placed_horses - initial_placed_horses

    return abs(cost)

def heuristic_function(board):
    rows, columns = np.shape(board)
    valid_positions = 0

    for i in range(rows):
        for j in range(columns):
            if is_valid_position(board, i, j):
                valid_positions += 1

    heuristic = -valid_positions

    return heuristic



def prune(path_list):
    result = []
    if len(path_list) == 0:
        return result
    rows, columns = np.shape(path_list[0][0])
    nodos = [np.zeros(shape=(rows, columns))]
    for path in path_list:
        if not np.any(np.all(path[0] == nodos, axis=(1,2))):
            nodos.append(path[0])
            result.append(path)

    return result


def equal_states(state, check_state):
    rows, columns = np.shape(state)
    for i in range(rows):
        for j in range(columns):
            if state[i][j] != check_state[i][j]:
                return False
    return True

def print_camino(c, coste=None, final=False):
  for j, s in enumerate(c):
    if j==0 and not coste is None:
      print(f'S{(j if final else len(c)-j-1)}: [g={coste}] \n{s}')
    else:
      print(f'S{(j if final else len(c)-j-1)}: \n{s}')

  print()

def order_astar(old_paths, new_paths, g, h, *args, **kwargs):
    cp = [[old_paths]]

    j = 0
    while cp:
        if not cp:
            return []

        if is_solution(cp[0][0]):
            return list(reversed(cp[0]))

        print(f'-- Paso {j} -- Caminos pendientes')
        for i, c in enumerate(cp):
            print(f'CP[{i}]: ')
            print_camino(c, g(c))

        expansion = new_paths(cp[0])
        print(f'-- Paso {j} -- Expandidos')
        for i, c in enumerate(expansion):
            print(f'E[{i}]: ')
            print_camino(c, g(c))

        unsrt = cp[1:] + expansion
        unsrt.sort(key=lambda x: g(x) + h(x[0]))
        cp = prune(unsrt)



        j+=1

    print("No se ha encontrado camino")
    return []

