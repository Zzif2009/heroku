import pygame, random, time, copy


class Board:
    def __init__(self, width=300, height=300):
        self.width = width
        self.height = height
        self.push = True
        self.board = [[0 for i in range(width)] for j in range(height)]
        self.left = 15
        self.top = 15
        self.cell_size = 30

    def set_view(self, left=15, top=15, cell_size=30):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for x in range(self.width):
            for y in range(self.height):
                pygame.draw.rect(screen, (255, 255, 255), (self.left + x * self.cell_size,
                                                           self.top + y * self.cell_size,
                                                           self.cell_size,
                                                           self.cell_size), 1)
                if self.board[y][x] == 1:
                    pygame.draw.rect(screen, (0, 255, 0), (self.left + y * self.cell_size + 1,
                                                           self.top + x * self.cell_size + 1,
                                                           self.cell_size - 1,
                                                           self.cell_size - 1), 0)

    def get_cell(self, mouse_pos):
        y, x = mouse_pos
        return ((x - self.left) // self.cell_size, (y - self.top) // self.cell_size)

    def on_click(self, cell_coords):
        x, y = cell_coords
        if self.board[y][x] == 0:
            self.board[y][x] = 1
        else:
            self.board[y][x] = 0

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        y, x = cell
        if x >= self.width or y >= self.height or x < 0 or y < 0:
            return 0
        self.on_click(cell)


class Life(Board):
    def __init__(self, n):
        super().__init__(n, n)

    def next_level(self):
        List = [[0 for i in range(self.width)] for j in range(self.height)]
        for x in range(self.height):
            for y in range(self.width):
                kol_near = self.board[x - 1][y]
                kol_near += self.board[(x + 1) % self.height][y]
                kol_near += self.board[x][y - 1]
                kol_near += self.board[x][(y + 1) % self.width]
                kol_near += self.board[x - 1][y - 1]
                kol_near += self.board[(x + 1) % self.height][(y + 1) % self.width]
                kol_near += self.board[x - 1][(y + 1) % self.width]
                kol_near += self.board[(x + 1) % self.height][y - 1]
                if kol_near == 3 or (self.board[x][y] == 1 and kol_near == 2):
                    List[x][y] = 1
        self.board = copy.deepcopy(List)
        self.push = False
        for x in range(self.width):
            for y in range(self.height):
                if self.board[y][x] == 1:
                    pygame.draw.rect(screen, (0, 255, 0), (self.left + y * self.cell_size + 1,
                                                           self.top + x * self.cell_size + 1,
                                                           self.cell_size - 1,
                                                           self.cell_size - 1), 0)

    def push_balls(self):
        self.push = True


def main(n):
    game = Life(n)
    running = True
    clock = pygame.time.Clock()
    game.render()
    fps = 5
    kol_space = 0
    next = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    fps += 1
                    kol_space = 0
                elif event.button == 5:
                    if fps > 1:
                        fps -= 1
                    kol_space = 0
                elif event.button == 3:
                    next = True
                    kol_space = 0
                elif event.button == 1 and game.push:
                    game.get_click(event.pos)
                    next = False
                    kol_space = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if kol_space == 1:
                        game.push_balls()
                        next = False
                    else:
                        next = True
                    kol_space = (kol_space + 1) % 2
        screen.fill((0, 0, 0))
        if next:
            game.next_level()
        game.render()
        pygame.display.flip()
        clock.tick(fps)
    return 0


n = int(input())
size = width, height = n * 30 + 30, n * 30 + 30
screen = pygame.display.set_mode(size)
pygame.init()
main(n)
pygame.quit()
