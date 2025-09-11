def print_args (*args):
    print(args)
    print(type(args))

print_args("30", "15", "random", "200", "0.2")

def seed_grid(func):
    def seed(*args, **kwargs):
        print("width, height, pattern")
        func(*args, **kwargs)
    return grid

def alive_neighbours(func):
    def neighbours(*args, **kwargs):
        print("grid, x, y")
        func(*args, **kwargs)
    return neighbours 

def cell_step(func):
    def steps(*args, **kwargs):
        print("grid")
        func(*args, **kwargs)
    return step

def cell_render(func):
    def render(*args, **kwargs):
        print("render")
        func(*args, **kwargs)
    return render

def cell_width (func):
    def info(*args, **kwargs):
        print("30")
        func(*args, **kwargs)
    return width

def cell_height (func):
    def info(*args, **kwargs):
        print("15")
        func(*args, **kwargs)
    return height
































