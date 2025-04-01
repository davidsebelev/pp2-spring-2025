import pygame
import math

def draw_line(screen, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    if iterations == 0:
        pygame.draw.circle(screen, color, start, width)
        return
    for i in range(iterations):
        p = i / iterations
        x = int((1 - p) * start[0] + p * end[0])
        y = int((1 - p) * start[1] + p * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint")
    clock = pygame.time.Clock()
    thickness = 15
    current_color = (0, 0, 255)
    current_tool = 'pencil'
    strokes = []
    shapes = []
    current_stroke = None
    shape_start = None
    shape_current = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_1:
                    current_tool = 'pencil'
                elif event.key == pygame.K_2:
                    current_tool = 'rectangle'
                elif event.key == pygame.K_3:
                    current_tool = 'circle'
                elif event.key == pygame.K_4:
                    current_tool = 'eraser'
                if event.key == pygame.K_b:
                    current_color = (0, 0, 255)
                elif event.key == pygame.K_r:
                    current_color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    current_color = (0, 255, 0)
                if event.key == pygame.K_UP:
                    thickness = min(200, thickness + 1)
                elif event.key == pygame.K_DOWN:
                    thickness = max(1, thickness - 1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if current_tool in ['pencil', 'eraser']:
                    col = current_color if current_tool == 'pencil' else (255, 255, 255)
                    current_stroke = {"points": [event.pos], "color": col, "thickness": thickness}
                elif current_tool in ['rectangle', 'circle']:
                    shape_start = event.pos
                    shape_current = event.pos
            if event.type == pygame.MOUSEMOTION:
                if current_tool in ['pencil', 'eraser']:
                    if current_stroke is not None and pygame.mouse.get_pressed()[0]:
                        current_stroke["points"].append(event.pos)
                elif current_tool in ['rectangle', 'circle']:
                    if shape_start is not None:
                        shape_current = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                if current_tool in ['pencil', 'eraser']:
                    if current_stroke is not None:
                        strokes.append(current_stroke)
                        current_stroke = None
                elif current_tool in ['rectangle', 'circle']:
                    if shape_start is not None:
                        s = {
                            "tool": current_tool,
                            "start": shape_start,
                            "end": event.pos,
                            "color": current_color,
                            "thickness": thickness
                        }
                        shapes.append(s)
                        shape_start = None
                        shape_current = None
        screen.fill((255, 255, 255))
        for stroke in strokes:
            pts = stroke["points"]
            for i in range(len(pts) - 1):
                draw_line(screen, pts[i], pts[i + 1], stroke["thickness"], stroke["color"])
        if current_stroke is not None:
            pts = current_stroke["points"]
            for i in range(len(pts) - 1):
                draw_line(screen, pts[i], pts[i + 1], current_stroke["thickness"], current_stroke["color"])
        for shape in shapes:
            if shape["tool"] == "rectangle":
                x1, y1 = shape["start"]
                x2, y2 = shape["end"]
                r = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
                pygame.draw.rect(screen, shape["color"], r, shape["thickness"])
            elif shape["tool"] == "circle":
                x1, y1 = shape["start"]
                x2, y2 = shape["end"]
                rad = int(math.hypot(x2 - x1, y2 - y1))
                pygame.draw.circle(screen, shape["color"], shape["start"], rad, shape["thickness"])
        if shape_start is not None and shape_current is not None:
            if current_tool == "rectangle":
                x1, y1 = shape_start
                x2, y2 = shape_current
                r = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
                pygame.draw.rect(screen, current_color, r, thickness)
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
