
# check the sudoku generation and solving
# algorithm in ../algorithm/sudoku.py

from pygame_utils import *

SIZE = 9

def isfilled(GRID):
    for row in GRID:
        if 0 in row:
            return False

    return True


def isvalid(GRID, pos):

    x, y = pos
    item = GRID[x][y]
    if GRID[x].count(item) > 1:
        return False

    counter = 0
    for i in range(SIZE):
        if GRID[i][y] == item:
            counter += 1
        if counter > 1:
            return False

    x = x - x % 3
    y = y - y % 3
    counter = 0
    for i in range(x, x + 3):
        counter += GRID[i][y: y + 3].count(item)
        if counter > 1:
            return False

    return True


def create_blanks(GRID):

    visited = set()
    counter = random.randrange(SIZE * 5, SIZE * 6)

    while counter:
        rand = random.randrange(SIZE ** 2)
        row = rand // SIZE
        col = rand - row * SIZE

        if (row, col) not in visited:
            GRID[row][col] = 0
            visited.add((row, col))
            counter -= 1


def generate_sudoku(GRID):

    nums = [x + 1 for x in range(SIZE)]

    for i in range(SIZE ** 2):
        row = i // SIZE
        col = i % SIZE
        if not GRID[row][col]:
            random.shuffle(nums)
            for value in nums:
                GRID[row][col] = value
                if isvalid(GRID, (row, col)):
                    if isfilled(GRID):
                        return True
                    else:
                        if generate_sudoku(GRID):
                            return True

                GRID[row][col] = 0
            break


# answers is a set containing all positions
def solve_sudoku(grid, pos, answers, positions, screen, button):

    GRID = grid.grid
    x, y = pos

    if x == SIZE:
        return True

    if y == SIZE:
        return solve_sudoku(grid, (x + 1, 0), answers, positions, screen, button)

    if GRID[x][y]:
        if solve_sudoku(grid, (x, y + 1), answers, positions, screen, button):
            return True
    else:
        for i in range(SIZE):
            if grid.render(button, answers, positions):
                return True
            grid.drawRect((x, y), i + 1, (Color.GREEN, Color.WHITE))
            pygame.display.update()

            GRID[x][y] = i + 1
            answers.append((x, y))

            if isvalid(GRID, pos) and solve_sudoku(grid, (x, y + 1), answers, positions, screen, button):
                return True

            GRID[x][y] = 0
            answers.remove((x, y))

    return False
