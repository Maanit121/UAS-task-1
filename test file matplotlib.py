grids = [
    ['S','.','#','.'],
    ['.','#','.','.'],
    ['.','.','.','G'],
]
ROWS = 3
COLS = 4
def grid_to_numbers(grid):
    numeric_grid = []
    for row in range(ROWS):
        new_row = []
        for col in range(COLS):
            if grid[row][col] == '#':
                new_row.append(1)
            else:
                new_row.append(0)
        numeric_grid.append(new_row)
    return numeric_grid

numeric_grids = grid_to_numbers(grids)
print(numeric_grids)

import matplotlib.pyplot as plt

plt.imshow(numeric_grids, cmap='gray_r')
plt.savefig('grid_only.png')