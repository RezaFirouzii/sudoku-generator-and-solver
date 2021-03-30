
# Sudoku solver and generator using "backtracking" algorithm

import random

GRID = []
SIZE = 9


# returns true if there is no empty spot in board
def isfilled():
    for row in GRID:
        if 0 in row:
            return False

    return True


# returns true if the value placed at row x and column y,
# passes all the conditions of a valid sudoku game
def isvalid(pos):

    x, y = pos
    item = GRID[x][y]
    if GRID[x].count(item) > 1:
        return False

    count = 0
    for i in range(SIZE):
        if GRID[i][y] == item:
            count += 1
        if count > 1:
            return False

    x = x - x % 3
    y = y - y % 3
    count = 0
    for i in range(x, x + 3):
        count += GRID[i][y: y + 3].count(item)
        if count > 1:
            return False
    
    return True


# creates blanks in table randomly for a random amount of time
def create_blanks():

    visited = set()  # a set stores empty spots
    count = random.randrange(SIZE * 5, SIZE * 6)

    while count:
        rand = random.randrange(SIZE ** 2)
        row = rand // SIZE
        col = rand - row * SIZE

        if (row, col) not in visited:
            GRID[row][col] = 0
            visited.add((row, col))
            count -= 1


# recursive function which backtracks for generating a valid sudoku
def generate_sudoku():

    nums = [x + 1 for x in range(SIZE)]

    for i in range(SIZE ** 2):
        row = i // SIZE
        col = i % SIZE
        if not GRID[row][col]:
            random.shuffle(nums)
            for value in nums:
                GRID[row][col] = value
                if isvalid((row, col)): 
                    if isfilled():
                        return True
                    else:
                        if generate_sudoku():
                            return True
                
                GRID[row][col] = 0                        
            break


# recursive function which backtrack to solve the sudoku
def solve_sudoku(pos=(0, 0)):
    x, y = pos
    
    if x == SIZE:
        return True

    if y == SIZE:
        return solve_sudoku((x + 1, 0))

    if GRID[x][y]:
        if solve_sudoku((x, y + 1)):
            return True
    else:
        for i in range(SIZE):
            GRID[x][y] = i + 1
            if isvalid(pos) and solve_sudoku((x, y + 1)):
                return True
            GRID[x][y] = 0

    return False
            

# driver code
if __name__ == "__main__":
    GRID = [([0] * SIZE) for _ in range(SIZE)]
    generate_sudoku()
    create_blanks()
    solve_sudoku()
    
    # output the table
    for row in GRID:
        print(row)


# give custom grid and
# solve it using solve_sudoku()

    # GRID = [
    #     [3, 0, 6, 5, 0, 8, 4, 0, 0], 
    #     [5, 2, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 8, 7, 0, 0, 0, 0, 3, 1], 
    #     [0, 0, 3, 0, 1, 0, 0, 8, 0], 
    #     [9, 0, 0, 8, 6, 3, 0, 0, 5], 
    #     [0, 5, 0, 0, 9, 0, 6, 0, 0], 
    #     [1, 3, 0, 0, 0, 0, 2, 5, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 7, 4], 
    #     [0, 0, 5, 2, 0, 6, 3, 0, 0]
    # ]
    # if solve_sudoku():
    #     print(GRID)
    # else:
    #     print("No solution found!")