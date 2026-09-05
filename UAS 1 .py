# To be done:

# Auto detect s/g positions from grid instead of typing them.    -Done
# track explored nodes not just final path
# matplotlib visulatisation
# written document explaining theory and results
#to convert character grid to numeric grid for matplotlib visualisation



grids = [
    ['S','.','#','.'],
    ['.','#','.','.'],
    ['.','.','.','G'],
]

ROWS = 3
COLS = 4

def find_position(grid, target_char):
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == target_char:
                return (row, col)

start = find_position(grids, 'S')
goal = find_position(grids, 'G')


def get_neigbours(pos):
    row, col = pos
    candidates = [
        (row - 1, col),  # Up
        (row + 1, col),  # Down
        (row, col - 1),  # Left
        (row, col + 1)   # Right
    ]

    neighbours = []
    for r, c in candidates:

        if 0 <= r < ROWS and 0 <= c < COLS and (grids[r][c] == '.' or grids[r][c] == 'G'):
            neighbours.append((r, c))

    return neighbours

print(get_neigbours(goal))

def heuristic(a, b):
    x1, y1 =a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)

print(heuristic(start, goal))


import heapq

open_set = []
heapq.heappush(open_set, (heuristic(start, goal), start))

g_score = {start: 0}
came_from = {}

while open_set:
    current_f, current = heapq.heappop(open_set)
    if current == goal:
     path = []
     while current in came_from:
         path.append(current)
         current = came_from[current]
     path.append(start)
     path.reverse()
     print("Path found:", path)
     break
        

    for neighbour in get_neigbours(current):
        tentative_g_score = g_score[current] + 1
        if neighbour not in g_score or tentative_g_score < g_score[neighbour]:
            came_from[neighbour] = current
            g_score[neighbour] = tentative_g_score
            heapq.heappush(open_set, (tentative_g_score + heuristic(neighbour, goal), neighbour))
            



    