import psycopg2
import pygame
import sys
import time
import random


def connect():
    return psycopg2.connect(
        dbname="snake_game_db", 
        user="postgres",        
        password="2106", 
        host="localhost"
    )


def create_tables():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            level INTEGER NOT NULL,
            score INTEGER NOT NULL,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Таблицы для Snake Game созданы.")

def get_or_create_user():
    username = input("Введите ваше имя для игры Snake: ").strip()
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user_row = cur.fetchone()
    if user_row:
        user_id = user_row[0]
        print(f"Добро пожаловать, {username}!")
        cur.execute("SELECT level, score FROM user_score WHERE user_id = %s ORDER BY last_updated DESC LIMIT 1", (user_id,))
        state = cur.fetchone()
        if state:
            level, score = state
            print(f"Ваш текущий уровень: {level}, счет: {score}")
        else:
            level = 1
            score = 0
            cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)", (user_id, level, score))
            conn.commit()
            print("Начинаем с 1 уровня и 0 очками.")
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        level = 1
        score = 0
        cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)", (user_id, level, score))
        conn.commit()
        print(f"Пользователь {username} создан. Игра началась с 1 уровня и 0 очками.")
    cur.close()
    conn.close()
    return user_id, level, score

def update_game_state(user_id, level, score):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)", (user_id, level, score))
    conn.commit()
    cur.close()
    conn.close()
    print("Состояние игры сохранено в БД.")


def get_walls(level, screen_width, screen_height, block_size):
    walls = []
    if level == 2:
  
        gap_height = 3 * block_size 
        gap_start = screen_height // 2 - gap_height // 2
 
        wall_top = pygame.Rect(screen_width // 2 - block_size // 2, 0, block_size, gap_start)
 
        wall_bottom = pygame.Rect(screen_width // 2 - block_size // 2, gap_start + gap_height, block_size, screen_height - (gap_start + gap_height))
        walls.extend([wall_top, wall_bottom])
    elif level == 3:
       
        wall1 = pygame.Rect(0, screen_height // 3 - block_size // 2, screen_width, block_size)
        wall2 = pygame.Rect(0, 2 * screen_height // 3 - block_size // 2, screen_width, block_size)
        walls.extend([wall1, wall2])
    elif level >= 4:
        wall1 = pygame.Rect(screen_width // 4 - block_size // 2, 0, block_size, screen_height)
        wall2 = pygame.Rect(3 * screen_width // 4 - block_size // 2, 0, block_size, screen_height)
        wall3 = pygame.Rect(0, screen_height // 2 - block_size // 2, screen_width, block_size)
        walls.extend([wall1, wall2, wall3])
    return walls


def main():
    create_tables() 
    user_id, current_level, current_score = get_or_create_user()

    pygame.init()
    screen_width = 600
    screen_height = 400
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Snake Game")

    clock = pygame.time.Clock()


    black = (0, 0, 0)
    green = (0, 255, 0)
    red = (255, 0, 0)
    white = (255, 255, 255)
    grey = (128, 128, 128)

    block_size = 20
    base_speed = 10  

 
    snake_pos = [100, 50]
    snake_body = [
        [100, 50],
        [80, 50],
        [60, 50]
    ]
    direction = 'RIGHT'
    change_to = direction


    def random_food():
        x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
        y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size
        return x, y

    food_x, food_y = random_food()

    score = current_score  
    level = current_level 

    font_style = pygame.font.SysFont(None, 35)


    def show_score(s, lvl):
        value = font_style.render(f"Score: {s}   Level: {lvl}", True, white)
        screen.blit(value, [0, 0])

    running = True
    paused = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
                elif event.key == pygame.K_UP:
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                elif event.key == pygame.K_p:
         
                    update_game_state(user_id, level, score)
                    paused = True
                    pause_font = pygame.font.SysFont(None, 50)
                    while paused:
                        for ev in pygame.event.get():
                            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_c:
                                paused = False
                        screen.fill((50, 50, 50))
                        pause_text = pause_font.render("Paused - Press C to continue", True, red)
                        screen.blit(pause_text, (screen_width / 6, screen_height / 2))
                        pygame.display.update()
                        clock.tick(5)

      
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'


        if direction == 'RIGHT':
            snake_pos[0] += block_size
        elif direction == 'LEFT':
            snake_pos[0] -= block_size
        elif direction == 'UP':
            snake_pos[1] -= block_size
        elif direction == 'DOWN':
            snake_pos[1] += block_size


        snake_body.insert(0, list(snake_pos))

     
        snake_rect = pygame.Rect(snake_pos[0], snake_pos[1], block_size, block_size)
        food_rect = pygame.Rect(food_x, food_y, block_size, block_size)

  
        walls = get_walls(level, screen_width, screen_height, block_size)

       
        if snake_rect.colliderect(food_rect):
            score += 10
            if score % 50 == 0:
                level += 1
            food_x, food_y = random_food()  
        else:
            snake_body.pop()

        
        screen.fill(black)
     
        for wall in walls:
            pygame.draw.rect(screen, grey, wall)
      
        for pos in snake_body:
            pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], block_size, block_size))
     
        pygame.draw.rect(screen, red, pygame.Rect(food_x, food_y, block_size, block_size))
        show_score(score, level)
        pygame.display.update()

        if (snake_pos[0] < 0 or snake_pos[0] >= screen_width or
            snake_pos[1] < 0 or snake_pos[1] >= screen_height):
            running = False

        
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                running = False

        for wall in walls:
            if snake_rect.colliderect(wall):
                running = False

       
        current_speed = base_speed + (level - 1) * 5
        clock.tick(current_speed)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
