import sys
from dfs import dfs
from ucs import ucs

def parse_world(file_path):
    with open(file_path, 'r', encoding='utf-16') as file:
        cols = int(file.readline().strip())
        rows = int(file.readline().strip())
        grid = [list(file.readline().strip()) for _ in range(rows)]
    
    start = None
    dirty = set()
    for r in range(rows):
        for c in range(cols):
            cell = grid[r][c]
            if cell == '@':
                start = (r, c)
            elif cell == '*':
                dirty.add((r, c))
    return grid, start, dirty



def main():
    if len(sys.argv) != 3:
        print("Usage: python3 planner.py [depth-first|uniform-cost] [world-file]")
        sys.exit(1)

    algorithm = sys.argv[1]
    file_path = sys.argv[2]

    grid, start, dirty = parse_world(file_path)

    if algorithm == 'depth-first':
        path, nodes_generated, nodes_expanded = dfs(grid, start, dirty)
    elif algorithm == 'uniform-cost':
        path, nodes_generated, nodes_expanded = ucs(grid, start, dirty)
    else:
        print("Invalid algorithm. Choose 'depth-first' or 'uniform-cost'.")
        sys.exit(1)

    for action in path:
        print(action)
    print(f"{nodes_generated} nodes generated")
    print(f"{nodes_expanded} nodes expanded")

if __name__ == "__main__":
    main()
