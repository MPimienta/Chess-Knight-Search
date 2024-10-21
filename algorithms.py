import dependent_functions as df

# Expands the current board of the given path
def expand(path):
    result = []
    successors = df.get_successors(path[0])

    for successor in successors:
        result.append(successor)

    return result