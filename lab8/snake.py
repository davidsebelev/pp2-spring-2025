import pygame, sys, random

# Инициализация Pygame
pygame.init()

# ------------------------- Настройки игры -------------------------
# Размер одного блока (ячейки) змейки и поля
BLOCK_SIZE = 20

# Размер поля в блоках (ширина и высота)
GRID_WIDTH = 30   # по горизонтали
GRID_HEIGHT = 20  # по вертикали

# Вычисление размера окна игры
SCREEN_WIDTH = GRID_WIDTH * BLOCK_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * BLOCK_SIZE

# Цвета (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)

# Создание игрового окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game with Levels")

# Настройка таймера для управления скоростью игры
clock = pygame.time.Clock()

# ------------------------- Инициализация игры -------------------------
# Задаём начальное положение змейки (список координат: (x, y))
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
# Начальное направление движения змейки (движется вправо)
direction = (1, 0)

# Функция для генерации случайной позиции еды
def get_random_food_position():
    """
    Генерирует случайную позицию для еды так,
    чтобы еда не появлялась на стене или на змейке.
    Стены находятся на границе поля, поэтому допустимые координаты - от 1 до GRID_WIDTH-2 и 1 до GRID_HEIGHT-2.
    """
    while True:
        x = random.randint(1, GRID_WIDTH - 2)
        y = random.randint(1, GRID_HEIGHT - 2)
        if (x, y) not in snake:  # Проверяем, чтобы еда не оказалась внутри змейки
            return (x, y)

# Начальное положение еды
food = get_random_food_position()

# Переменные для счета и уровня
score = 0
level = 1
# Начальная скорость (количество кадров в секунду)
speed = 10

# ------------------------- Функции отрисовки -------------------------
def draw_walls():
    """
    Рисует стены (границы) игрового поля.
    Стены располагаются по периметру экрана и обозначаются красным цветом.
    """
    # Верхняя стена
    pygame.draw.rect(screen, RED, (0, 0, SCREEN_WIDTH, BLOCK_SIZE))
    # Нижняя стена
    pygame.draw.rect(screen, RED, (0, SCREEN_HEIGHT - BLOCK_SIZE, SCREEN_WIDTH, BLOCK_SIZE))
    # Левая стена
    pygame.draw.rect(screen, RED, (0, 0, BLOCK_SIZE, SCREEN_HEIGHT))
    # Правая стена
    pygame.draw.rect(screen, RED, (SCREEN_WIDTH - BLOCK_SIZE, 0, BLOCK_SIZE, SCREEN_HEIGHT))

def display_score_level():
    """
    Отображает счет и уровень в верхней части экрана.
    """
    font = pygame.font.SysFont("Arial", 24)
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (BLOCK_SIZE, BLOCK_SIZE))

# ------------------------- Основной игровой цикл -------------------------
game_over = False
while not game_over:
    # Обработка событий (нажатия клавиш, закрытие окна и т.д.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Обработка нажатий клавиш для управления направлением змейки
        elif event.type == pygame.KEYDOWN:
            # Проверяем, чтобы змейка не могла повернуть на 180 градусов
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)
    
    # Вычисляем новое положение головы змейки
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])
    
    # ------------------------- Проверка столкновений -------------------------
    # Проверка столкновения с границами поля (стенами)
    # Если координата головы меньше или равна 0 или больше или равна GRID_WIDTH-1 (так как стены занимают крайние блоки) -> игра окончена.
    if new_head[0] <= 0 or new_head[0] >= GRID_WIDTH - 1 or new_head[1] <= 0 or new_head[1] >= GRID_HEIGHT - 1:
        game_over = True
        break
    
    # Проверка столкновения со своим телом
    if new_head in snake:
        game_over = True
        break
    
    # Вставляем новую голову в начало списка (движение змейки)
    snake.insert(0, new_head)
    
    # Если змейка съела еду
    if new_head == food:
        score += 1  # увеличиваем счет
        # Каждые 3 съеденных еды повышаем уровень
        if score % 3 == 0:
            level += 1
            speed += 2  # увеличиваем скорость игры
        # Генерируем новую позицию для еды
        food = get_random_food_position()
    else:
        # Если еда не съедена, убираем последний элемент змейки (движение без роста)
        snake.pop()
    
    # ------------------------- Отрисовка объектов -------------------------
    # Заливаем фон чёрным цветом
    screen.fill(BLACK)
    
    # Рисуем стены (границы)
    draw_walls()
    
    # Рисуем змейку: каждый сегмент змейки – это прямоугольник
    for segment in snake:
        rect = pygame.Rect(segment[0] * BLOCK_SIZE, segment[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(screen, GREEN, rect)
    
    # Рисуем еду
    food_rect = pygame.Rect(food[0] * BLOCK_SIZE, food[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.rect(screen, WHITE, food_rect)
    
    # Отображаем счет и уровень
    display_score_level()
    
    # Обновляем экран
    pygame.display.flip()
    # Задаем задержку, управляющую скоростью игры
    clock.tick(speed)

# ------------------------- Конец игры -------------------------
# Выводим сообщение "Game Over"
font = pygame.font.SysFont("Arial", 48)
game_over_text = font.render("Game Over", True, RED)
screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2,
                             SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
pygame.display.flip()
# Ждем 2 секунды, чтобы игрок увидел сообщение
pygame.time.wait(2000)
pygame.quit()
sys.exit()
