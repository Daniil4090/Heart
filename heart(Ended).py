screen = []
screen_size = 41
center = screen_size // 2

def draw_pixel(sym):
    try:
        print(sym * 2, end="")
    except:
        pass

def F(x):
    return (x ** 2) ** (1/3) + (1 - x**2) ** (1/2)

def F2(x):
    return (x ** 2) ** (1/3) - (1 - x**2) ** (1/2)

for y in range(screen_size):
    line = []
    for x in range(screen_size):
        line.append("\033[46m \033[0m")
    screen.append(line)

screen[center][center] = "\033[46m \033[0m"

for i in range(-15, 16):
    x = i / 15
    print(F(x))
    y1 = -int((F2(x) * 15)) + center + 4
    y2 = -int((F(x) * 15)) + center + 4
    for y in range(y2, y1):
        screen[y][i + center] = "\033[41m \033[0m"

for i in range(-12, 13):
    x = i / 12
    print(F(x))
    y1 = -int((F2(x) * 12)) + center + 4
    y2 = -int((F(x) * 12)) + center + 4
    for y in range(y2, y1):
        screen[y][i + center] = "\033[46m \033[0m"

for i in range(-10, 11):
    x = i / 10
    print(F(x))
    y1 = -int((F2(x) * 10)) + center + 4
    y2 = -int((F(x) * 10)) + center + 4
    for y in range(y2, y1):
        screen[y][i + center] = "\033[45m \033[0m"
    
for i in range(-8, 9):
    x = i / 8
    print(F(x))
    y1 = -int((F2(x) * 8)) + center + 3
    y2 = -int((F(x) * 8)) + center + 3
    for y in range(y2, y1):
        screen[y][i + center] = "\033[41m \033[0m"

for y in range(screen_size):
    for x in range(screen_size):
        draw_pixel(screen[y][x])
    print()
