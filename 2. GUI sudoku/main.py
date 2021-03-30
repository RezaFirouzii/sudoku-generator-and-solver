from sudoku import *
from pygame_utils import *
import os

# GUI Constants
TITLE = "Sudoku generator and solver"
WINDOWS_LOCATION = '350,70'
SIZE = 9
WIDTH = 650
HEIGHT = 650
CELL_SIZE = 71
FPS = 10


def run_game():
    
    # 1st loop: visualizes how sudoku is being generated 
    running = True

    title = 'Generate!'
    button = Box((screen.get_width() - len(title) * 14) // 2, 10, len(title) * 14, 50, title)
    pressed = False         # shows whether button is pressed or not

    positions = set()
    row, col = 0, 0
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                return

            if button.handle_event(event):
                pressed = True
                button.text = "Generating Sudoku..."
                generate_sudoku(grid.grid)
                create_blanks(grid.grid)

        screen.fill(Color.WHITE)
        button.draw(screen, pressed, Color.RED)
        if pressed:
            positions.add((row, col))
            col += 1
            if col == SIZE:
                col = 0
                row += 1
            if row == SIZE:
                running = False
        grid.drawUseRect(positions)
        pygame.display.update()


    # 2nd loop: visualizes how sudoku is being solved
    title = 'Solve!'
    button = Box((screen.get_width() - len(title) * 14) // 2, 10, len(title) * 14, 50, title)
    pressed = False
    running = True

    finished = False
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

            if button.handle_event(event):
                pressed = True
                button.text = "Solving Sudoku..."

        screen.fill(Color.WHITE)
        button.draw(screen, pressed, Color.GREEN)
        grid.drawUseRect(positions, finished)
        pygame.display.update()

        if pressed:
            # solving sudoku
            if solve_sudoku(grid, (0, 0), [], positions, screen, button):
                finished = True
            else:
                running = False

        if finished:
            screen.fill(Color.WHITE)
            button.text = 'Sudoku is solved successfully :)'
            button.draw(screen, pressed, Color.GREEN)
            grid.drawUseRect(positions, True)
            pygame.display.update()


if __name__ == '__main__':
    # setting Pygame window position
    os.environ['SDL_VIDEO_WINDOW_POS'] = WINDOWS_LOCATION

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT + CELL_SIZE))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    CELL_SIZE = HEIGHT // SIZE
    grid = Grid(surface=screen, cellSize=CELL_SIZE)

    run_game()

    pygame.quit()
