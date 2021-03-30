
# bunch of useful classes made using pygame methods

import pygame
import random


# represents a button
class Box:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = Color.BLACK
        self.text = text
        self.txt_surface = pygame.font.Font(None, 32).render(text, True, Color.WHITE)

    # if button is clicked
    def handle_event(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN

    # drawing button
    def draw(self, screen, pressed, color):
        if not pressed:
            screen.fill(color, self.rect)
            pygame.draw.rect(screen, self.color, self.rect, 2)
            screen.blit(self.txt_surface, (self.rect.x + 10, self.rect.y + 15))
        else:
            self.txt_surface = pygame.font.Font(None, 32).render(self.text, True, color)
            screen.blit(self.txt_surface, (self.rect.x - 50, self.rect.y + 15))


# sudoku table
class Grid:

    def __init__(self, surface, cellSize):
        self.surface = surface
        self.rows = 9
        self.cols = 9
        self.cellSize = cellSize
        self.grid = [([0] * self.cols) for _ in range(self.rows)]

    def drawRect(self, pos, value, color):
        row, col = pos
        fill, clr = color

        rect = pygame.Rect(col * self.cellSize, (row + 1) * self.cellSize, self.cellSize, self.cellSize)
        self.surface.fill(fill, rect)
        pygame.draw.rect(self.surface, Color.BLACK, rect, 1)

        font = pygame.font.SysFont('arial', 60 - 2 * self.rows - len(str(self.rows)) * 5, True)
        text = font.render(str(value), True, clr)
        coord = (3 * self.cellSize) // 10
        self.surface.blit(text, (col * self.cellSize + coord + 5, (row + 1) * self.cellSize + coord - 5))

    def drawUseRect(self, positions, finished=False):
        for row in range(self.rows):
            x_axis = row * self.cellSize
            for col in range(self.cols):

                y_axis = (col + 1) * self.cellSize
                rect = pygame.Rect(x_axis, y_axis, self.cellSize, self.cellSize)
                pygame.draw.rect(self.surface, Color.BLACK, rect, 1)
                if len(positions) and (row, col) in positions:
                    if self.grid[row][col]:
                        color = Color.GREEN if finished else Color.RED
                        self.drawRect((row, col), self.grid[row][col], (color, Color.WHITE))
                    else:
                        self.drawRect((row, col), '?', (Color.WHITE, Color.RED))


    # rendering the screen while solving sudoku
    def render(self, button, answers, positions):
        pygame.time.Clock().tick(15)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                quit(0)

        self.surface.fill(Color.WHITE)
        button.draw(self.surface, True, Color.GREEN)
        self.drawUseRect(positions)
        for position in answers:
            row, col = position
            self.drawRect(position, self.grid[row][col], (Color.GREEN, Color.WHITE))

        return False


class Color:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 128, 255)
    GREEN = (0, 153, 0)
    YELLOW = (255, 255, 0)
    BROWN = (204, 102, 0)
    PINK = (255, 102, 178)
    PURPLE = (153, 51, 255)

    colors = {
        1: WHITE,
        2: YELLOW,
        3: RED,
        4: BLUE,
        5: GREEN,
        6: BLACK,
        7: BROWN,
        8: PINK,
        9: PURPLE,
    }
