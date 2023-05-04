from collections import deque
from PIL import Image, ImageDraw

BOARD_SIZE = 8
ALLOWED_FIELDS = set((x, y) for x in range(BOARD_SIZE) for y in range(BOARD_SIZE))
ALLOWED_KNIGHT_MOVES = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]


def calculate_path(start: tuple, target: tuple):
    """
    calculates the shortest route of a knight in a game of chess
    :param start: the starting position
    :param target: the target posiiton
    :return:
    """
    frontier = deque()
    frontier.append(start)
    parents = {start: None}

    while frontier:
        current = frontier.popleft()
        if current == target:
            break
        for move in ALLOWED_KNIGHT_MOVES:
            next_pos = (current[0] + move[0], current[1] + move[1])
            if next_pos in ALLOWED_FIELDS and next_pos not in parents:
                frontier.append(next_pos)
                parents[next_pos] = current

    path = []
    current = target
    while current != start:
        path.append(current)
        current = parents[current]
    path.append(start)
    path.reverse()

    return path


def draw_board(path: list[tuple[int, int]]):
    """
    draws a chess board with the route of the knight
    :param path: the route the knight takes
    :return: a chess board
    """
    cell_size = 50
    board_size = cell_size * BOARD_SIZE
    img = Image.new('RGB', (board_size, board_size), color='white')
    draw = ImageDraw.Draw(img)

    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if (x + y) % 2 == 0:
                draw.rectangle((x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size), fill='gray')

    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        draw.line(((x1 + 0.5) * cell_size, (y1 + 0.5) * cell_size, (x2 + 0.5) * cell_size, (y2 + 0.5) * cell_size),
                  fill='red', width=5)

    x, y = path[0]
    draw.ellipse(((x + 0.2) * cell_size, (y + 0.2) * cell_size, (x + 0.8) * cell_size, (y + 0.8) * cell_size),
                 fill='black')

    img.save("knight.png")


if __name__ == '__main__':
    start = (0, 0)
    target = (4, 4)

    draw_board(calculate_path(target, start))
