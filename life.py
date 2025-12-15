import pygame
pygame.init()

if __name__ == "__Game_Of_Life__":
    pygame.init()

# Set up the game window
surface = pygame.display.set_mode((1200, 900))
pygame.display.is_fullscreen()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()

def print_args (*args):
    print(args)
    print(type(args))

print_args("30", "15", "random", "200", "0.2")

def seed_grid(func):
    def grid(*args, **kwargs):
        print("width, height, pattern")
        func(*args, **kwargs)
    return grid

def alive_neighbors(func):
    def neighbors(*args, **kwargs):
        print("grid, x, y")
        func(*args, **kwargs)
    return neighbors

def step(func):
    def steps(*args, **kwargs):
        print("grid")
        func(*args, **kwargs)
    return steps

def render(func):
    def info(*args, **kwargs):
        print("grid")
        func(*args, **kwargs)
    return render

def width(func):
    def info(*args, **kwargs):
        print("30")
        func(*args, **kwargs)
    return info

def height(func):
    def info(*args, **kwargs):
        print("15")
        func(*args, **kwargs)
    return info

def pattern(func):
    def info(*args, **kwargs):
        print("random")
        func(*args, **kwargs)
    return info

def steps(func):
    def info(*args, **kwargs):
        print("200")
        func(*args, **kwargs)
    return info

def delay(func):
    def info(*args, **kwargs):
        print("0.2")
        func(*args, **kwargs)
    return info




















































































