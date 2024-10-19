import methods

board = methods.initial_state(3, 3)
print(board)
boards = methods.expand(board)
for b in boards:
    print(b)

