import pygame, sys, random, time
pygame.init()
BLOCK_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
SCREEN_WIDTH = GRID_WIDTH * BLOCK_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * BLOCK_SIZE
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
direction = (1, 0)
foods = []
score = 0
level = 1
speed = 10
font_small = pygame.font.SysFont("Arial", 24)
def spawn_food():
    while True:
        x = random.randint(1, GRID_WIDTH - 2)
        y = random.randint(1, GRID_HEIGHT - 2)
        if (x, y) not in snake:
            w = random.randint(1, 5)
            return {"pos": (x, y), "weight": w, "spawn": time.time()}
for _ in range(2):
    foods.append(spawn_food())
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)
    hx, hy = snake[0]
    new_head = (hx + direction[0], hy + direction[1])
    if new_head[0] <= 0 or new_head[0] >= GRID_WIDTH - 1 or new_head[1] <= 0 or new_head[1] >= GRID_HEIGHT - 1:
        game_over = True
        break
    if new_head in snake:
        game_over = True
        break
    snake.insert(0, new_head)
    eaten = False
    for f in foods[:]:
        if new_head == f["pos"]:
            score += f["weight"]
            if score % 3 == 0:
                level += 1
                speed += 2
            foods.remove(f)
            foods.append(spawn_food())
            eaten = True
            break
    if not eaten:
        snake.pop()
    now = time.time()
    for f in foods[:]:
        if now - f["spawn"] > 5:
            foods.remove(f)
            foods.append(spawn_food())
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (0, 0, SCREEN_WIDTH, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, (0, SCREEN_HEIGHT - BLOCK_SIZE, SCREEN_WIDTH, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, (0, 0, BLOCK_SIZE, SCREEN_HEIGHT))
    pygame.draw.rect(screen, RED, (SCREEN_WIDTH - BLOCK_SIZE, 0, BLOCK_SIZE, SCREEN_HEIGHT))
    for s in snake:
        pygame.draw.rect(screen, GREEN, (s[0] * BLOCK_SIZE, s[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    for f in foods:
        pygame.draw.rect(screen, WHITE, (f["pos"][0] * BLOCK_SIZE, f["pos"][1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    txt = font_small.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(txt, (BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.flip()
    clock.tick(speed)
f = pygame.font.SysFont("Arial", 48)
over_text = f.render("Game Over", True, RED)
screen.blit(over_text, (SCREEN_WIDTH // 2 - over_text.get_width() // 2, SCREEN_HEIGHT // 2 - over_text.get_height() // 2))
pygame.display.flip()
pygame.time.wait(2000)
pygame.quit()
sys.exit()
