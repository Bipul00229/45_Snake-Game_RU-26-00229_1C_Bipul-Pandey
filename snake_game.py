import pygame
import random
import sys
pygame.init()
size = 10
cell = 50
width = size * cell
height = size * cell
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
gray = (200, 200, 200)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)
snake = [(5, 5)]
food_list = [(7, 5), (0, 0)]
food_no = 0
food = food_list[0]
direction = "R"
score = 0
game_over = False
def new_food():
    global food_no
    food_no = food_no + 1
    if food_no < len(food_list):
        return food_list[food_no]
    while True:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        if (x, y) not in snake:
            return (x, y)
def draw_grid():
    for x in range(0, width, cell):
        pygame.draw.line(screen, gray, (x, 0), (x, height))
    for y in range(0, height, cell):
        pygame.draw.line(screen, gray, (0, y), (width, y))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and game_over == False:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            key = event.key
            if key == pygame.K_RIGHT or key == pygame.K_r:
                new_direction = "R"
            elif key == pygame.K_LEFT or key == pygame.K_l:
                new_direction = "L"
            elif key == pygame.K_UP or key == pygame.K_u:
                new_direction = "U"
            elif key == pygame.K_DOWN or key == pygame.K_d:
                new_direction = "D"
            else:
                print("Invalid key. Use R, L, U or D.")
                new_direction = direction
            if new_direction == "R" and direction == "L":
                print("Reverse move not allowed.")
            elif new_direction == "L" and direction == "R":
                print("Reverse move not allowed.")
            elif new_direction == "U" and direction == "D":
                print("Reverse move not allowed.")
            elif new_direction == "D" and direction == "U":
                print("Reverse move not allowed.")
            else:
                direction = new_direction
    if game_over == False:
        x = snake[0][0]
        y = snake[0][1]
        if direction == "R":
            x = x + 1
        elif direction == "L":
            x = x - 1
        elif direction == "U":
            y = y - 1
        elif direction == "D":
            y = y + 1
        new_head = (x, y)
        if x < 0 or x >= size or y < 0 or y >= size:
            game_over = True
            print("Game Over! Wall hit at", new_head)
            print("Final score:", score)
        elif new_head in snake:
            game_over = True
            print("Game Over! Self collision.")
            print("Final score:", score)
        else:
            snake.insert(0, new_head)
            print("Head:", new_head)
            if new_head == food:
                score = score + 10
                print("Food eaten at", food)
                print("Score:", score)
                print("Length:", len(snake))
                print("Head:", new_head)
                food = new_food()
            else:
                snake.pop()
    screen.fill(black)
    draw_grid()
    pygame.draw.rect(
        screen,
        red,
        (food[0] * cell, food[1] * cell, cell, cell)
    )
    for part in snake:
        pygame.draw.rect(
            screen,
            green,
            (part[0] * cell, part[1] * cell, cell, cell)
        )
    if game_over == True:
        msg = font.render(
            "GAME OVER! Score: " + str(score),
            True,
            white
        )
    else:
        msg = font.render(
            "Score: " + str(score),
            True,
            white
        )
    screen.blit(msg, (10, 10))
    pygame.display.update()
    clock.tick(3)