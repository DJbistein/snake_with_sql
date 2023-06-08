#new snake game

#TESTING
#cgvcgsvc

# update snake file

import pygame
import random
import time
import pymssql

server = "192.168.15.15\\IT22"
login = "sa"
password = "123QWEr"
database = "db_jj_1im"

def ADD_HIGH_SCORE(score, name):
    conn = pymssql.connect(server, login, password)
    conn.autocommit(True)
    usedb = f"USE {database}"
    cursor = conn.cursor()
    cursor.execute(usedb)
    sqlline = f"INSERT INTO snake_hs (score, name) VALUES ({score}, '{name}');"
    cursor.execute(sqlline)
    conn.close()


pygame.init()

# farger
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (255, 132, 203)
RED = (255, 0, 0)
BACKGROUNDCOLOR = (100, 100, 255)

CELL_SIZE = 60
CELL_NUMBER = 15

HEIGHT = CELL_SIZE * CELL_NUMBER
WIDTH = CELL_SIZE * CELL_NUMBER

fps = 60
colck = pygame.time.Clock()

screen = pygame.display.set_mode((HEIGHT, WIDTH))


class Snake:
    def __init__(self):
        self.dir = "r"
        self.body = [
            [7 * CELL_SIZE, 7 * CELL_SIZE, CELL_SIZE, CELL_SIZE],
            [6 * CELL_SIZE, 7 * CELL_SIZE, CELL_SIZE, CELL_SIZE],
            [5 * CELL_SIZE, 7 * CELL_SIZE, CELL_SIZE, CELL_SIZE]
        ]
        self.color = GREEN
        self.timer = round(time.time() * 1000)
        self.speed = 500
        self.score = 0

    def draw(self):
        for block in self.body:
            pygame.draw.rect(screen, self.color, block)

    def move(self):
        if self.timer < round(time.time() * 1000) - self.speed:
            newHead = self.body.pop()
            newHead[0] = self.body[0][0]
            newHead[1] = self.body[0][1]
            if self.dir == "r":
                newHead[0] += 1 * CELL_SIZE
            elif self.dir == "l":
                newHead[0] -= 1 * CELL_SIZE
            elif self.dir == "d":
                newHead[1] += 1 * CELL_SIZE
            else:
                newHead[1] -= 1 * CELL_SIZE

            self.body.insert(0, newHead)
            self.timer = round(time.time() * 1000)

    def add_block(self):
        newBlock = self.body[-1].copy()
        self.body.insert(-1, newBlock)
        self.speed -= 30
        self.score += 5

    def reset_game(self):
        ADD_HIGH_SCORE(self.score, "jostein")
        self.body = [
            [7 * CELL_SIZE, 7 * CELL_SIZE, CELL_SIZE, CELL_SIZE],
            [6 * CELL_SIZE, 7 * CELL_SIZE, CELL_SIZE, CELL_SIZE],
            [5 * CELL_SIZE, 7 * CELL_SIZE, CELL_SIZE, CELL_SIZE]
        ]
        self.speed = 500
        self.dir = "r"


class Apple:
    def __init__(self):
        self.height = CELL_SIZE
        self.widht = CELL_SIZE
        self.xPos = random.randint(0, 14) * CELL_SIZE
        self.yPos = random.randint(0, 14) * CELL_SIZE
        self.color = RED

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.xPos, self.yPos, self.height, self.widht))


def draw_score(tall):
    myFont = pygame.font.SysFont("monospace", 38)
    label = myFont.render(f"score: {tall}", 1, BLACK)
    screen.blit(label, (20, 20))

def draw_highscore(tall):
    myFont = pygame.font.SysFont("monospace", 18)
    label = myFont.render(f"HighScore: {tall}", 1, BLACK)
    screen.blit(label, (WIDTH - 200, HEIGHT - 50))


def collide():
    if snake.body[0][0] == apple.xPos and snake.body[0][1] == apple.yPos:
        apple.xPos = random.randint(0, 14) * CELL_SIZE
        apple.yPos = random.randint(0, 14) * CELL_SIZE
        snake.add_block()
    if snake.body[0][0] > WIDTH - 1 * CELL_SIZE:
        snake.reset_game()
    elif snake.body[0][1] > HEIGHT - 1 * CELL_SIZE:
        snake.reset_game()
    elif snake.body[0][1] < 0:
        snake.reset_game()
    elif snake.body[0][0] < 0:
        snake.reset_game()
    for block in snake.body[1:]:
        if snake.body[0][0] == block[0] and snake.body[0][1] == block[1]:
            snake.reset_game()


def draw_cells():
    for x in range(CELL_NUMBER):
        pygame.draw.line(screen, BLACK, (x * CELL_SIZE, 0), (x * CELL_SIZE, HEIGHT))
        pygame.draw.line(screen, BLACK, (0, x * CELL_SIZE), (WIDTH, x * CELL_SIZE))


def update():
    screen.fill(BACKGROUNDCOLOR)
    snake.draw()
    snake.move()
    apple.draw()
    draw_score(snake.score)
    draw_highscore(snake.score)
    collide()
    pygame.display.update()


snake = Snake()
apple = Apple()

main = True
while main:
    colck.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                main = False
            elif event.key == pygame.K_LEFT:
                if snake.dir != "a":
                    snake.dir = "l"
            elif event.key == pygame.K_RIGHT:
                if snake.dir != "d":
                    snake.dir = "r"
            elif event.key == pygame.K_UP:
                if snake.dir != "w":
                    snake.dir = "u"
            elif event.key == pygame.K_DOWN:
                if snake.dir != "u":
                    snake.dir = "d"

    update()