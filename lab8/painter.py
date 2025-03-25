import pygame
import math

# Функция для рисования линии между двумя точками с заданной толщиной и цветом
def draw_line(screen, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    if iterations == 0:
        pygame.draw.circle(screen, color, start, width)
        return
    for i in range(iterations):
        progress = i / iterations
        x = int((1 - progress) * start[0] + progress * end[0])
        y = int((1 - progress) * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def main():
    pygame.init()
    # Размер окна и фон (белый, чтобы ластик «стирал» содержимое)
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Расширенный рисовальщик")
    clock = pygame.time.Clock()

    # Начальные значения толщины, текущего цвета и выбранного инструмента
    thickness = 15
    current_color = (0, 0, 255)  # синий по умолчанию
    current_tool = 'pencil'      # доступные: 'pencil', 'rectangle', 'circle', 'eraser'

    # Списки для сохранения нарисованных объектов
    strokes = []      # свободные линии (карандаш или ластик)
    shapes = []       # прямоугольники и круги

    # Переменные для текущего штриха (карандаш/ластик)
    current_stroke = None

    # Переменные для рисования фигур (прямоугольник или круг)
    shape_start = None   # точка начала фигуры
    shape_current = None # текущая позиция мыши для предпросмотра

    running = True
    while running:
        for event in pygame.event.get():
            # Завершение работы при закрытии окна или нажатием ESC
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                # Выбор инструмента (клавиши 1-4)
                if event.key == pygame.K_1:
                    current_tool = 'pencil'
                    print("Выбран инструмент: карандаш")
                elif event.key == pygame.K_2:
                    current_tool = 'rectangle'
                    print("Выбран инструмент: прямоугольник")
                elif event.key == pygame.K_3:
                    current_tool = 'circle'
                    print("Выбран инструмент: круг")
                elif event.key == pygame.K_4:
                    current_tool = 'eraser'
                    print("Выбран инструмент: ластик")

                # Выбор цвета (работает для карандаша и фигур)
                if event.key == pygame.K_b:
                    current_color = (0, 0, 255)
                    print("Выбран цвет: синий")
                elif event.key == pygame.K_r:
                    current_color = (255, 0, 0)
                    print("Выбран цвет: красный")
                elif event.key == pygame.K_g:
                    current_color = (0, 255, 0)
                    print("Выбран цвет: зелёный")

                # Регулировка толщины с помощью стрелок вверх/вниз
                if event.key == pygame.K_UP:
                    thickness = min(200, thickness + 1)
                    print("Толщина увеличена:", thickness)
                elif event.key == pygame.K_DOWN:
                    thickness = max(1, thickness - 1)
                    print("Толщина уменьшена:", thickness)

            # Обработка нажатия мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Для карандаша и ластика начинаем новый штрих
                if current_tool in ['pencil', 'eraser']:
                    # В режиме ластика цвет = цвет фона (белый)
                    stroke_color = current_color if current_tool == 'pencil' else (255, 255, 255)
                    current_stroke = {"points": [event.pos], "color": stroke_color, "thickness": thickness}
                # Для фигур запоминаем начальную точку
                elif current_tool in ['rectangle', 'circle']:
                    shape_start = event.pos
                    shape_current = event.pos

            if event.type == pygame.MOUSEMOTION:
                # Если зажат левый клик (рисуем штрих)
                if current_tool in ['pencil', 'eraser']:
                    if current_stroke is not None and pygame.mouse.get_pressed()[0]:
                        current_stroke["points"].append(event.pos)
                # Для фигур обновляем текущую позицию для предпросмотра
                elif current_tool in ['rectangle', 'circle']:
                    if shape_start is not None:
                        shape_current = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                # Завершаем штрих для карандаша или ластика
                if current_tool in ['pencil', 'eraser']:
                    if current_stroke is not None:
                        strokes.append(current_stroke)
                        current_stroke = None
                # Завершаем рисование фигуры
                elif current_tool in ['rectangle', 'circle']:
                    if shape_start is not None:
                        # Сохраняем фигуру как словарь
                        shape = {
                            "tool": current_tool,
                            "start": shape_start,
                            "end": event.pos,
                            "color": current_color,
                            "thickness": thickness
                        }
                        shapes.append(shape)
                        shape_start = None
                        shape_current = None

        # Заливка фона (белый)
        screen.fill((255, 255, 255))

        # Рисуем сохранённые штрихи (карандаш или ластик)
        for stroke in strokes:
            pts = stroke["points"]
            for i in range(len(pts) - 1):
                draw_line(screen, pts[i], pts[i + 1], stroke["thickness"], stroke["color"])
        # Если в данный момент рисуем штрих – выводим его предпросмотр
        if current_stroke is not None:
            pts = current_stroke["points"]
            for i in range(len(pts) - 1):
                draw_line(screen, pts[i], pts[i + 1], current_stroke["thickness"], current_stroke["color"])

        # Рисуем сохранённые фигуры (прямоугольники и круги)
        for shape in shapes:
            if shape["tool"] == "rectangle":
                x1, y1 = shape["start"]
                x2, y2 = shape["end"]
                rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
                pygame.draw.rect(screen, shape["color"], rect, shape["thickness"])
            elif shape["tool"] == "circle":
                x1, y1 = shape["start"]
                x2, y2 = shape["end"]
                # Вычисляем радиус как расстояние между точками
                rad = int(math.hypot(x2 - x1, y2 - y1))
                pygame.draw.circle(screen, shape["color"], shape["start"], rad, shape["thickness"])

        # Если фигура в процессе рисования – показываем её предпросмотр
        if shape_start is not None and shape_current is not None:
            if current_tool == "rectangle":
                x1, y1 = shape_start
                x2, y2 = shape_current
                preview_rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
                pygame.draw.rect(screen, current_color, preview_rect, thickness)
            elif current_tool == "circle":
                x1, y1 = shape_start
                x2, y2 = shape_current
                rad = int(math.hypot(x2 - x1, y2 - y1))
                pygame.draw.circle(screen, current_color, shape_start, rad, thickness)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
