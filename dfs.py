ACTIONS = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1),
    'V': (0, 0),  # Vacuum
}

def dfs(grid, start, dirty_cells):
    stack = [(start, frozenset(dirty_cells), [])]
    visited = set()
    nodes_generated = 0
    nodes_expanded = 0
    rows, cols = len(grid), len(grid[0])

    while stack:
        position, dirt, path = stack.pop()
        state = (position, dirt)

        if state in visited:
            continue
        visited.add(state)
        nodes_expanded += 1

        if not dirt:
            return path, nodes_generated, nodes_expanded

        cur_row, cur_col = position

        # Vacuum first if dirty
        if position in dirt:
            new_dirt = set(dirt)
            new_dirt.remove(position)
            stack.append((position, frozenset(new_dirt), path + ['V']))
            nodes_generated += 1

        # test moving all direction
        for action, (delta_row, delta_col) in ACTIONS.items():
            if action == 'V':
                continue  # test if just vacuumed
            next_row = cur_row + delta_row
            next_col = cur_col + delta_col
            if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] != '#':
                new_pos = (next_row, next_col)
                stack.append((new_pos, dirt, path + [action]))
                nodes_generated += 1

    print("No Solution Found")
    return [], nodes_generated, nodes_expanded  # No solution
