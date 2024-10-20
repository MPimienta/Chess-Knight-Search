import methods

board = methods.initial_state(4,5 )

print(board)
final_path = methods.order_astar(board,methods.expand,methods.cost_function, methods.heuristic_function)
print("------------FINAL------------")
methods.print_camino(final_path, methods.cost_function(final_path), final=True)

