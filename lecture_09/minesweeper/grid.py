"""
DOC
ASDSTRING
"""
import sys
import random


def generate_coordinate(x_dim, y_dim):
    x = random.randint(0, x_dim - 1)
    y = random.randint(0, y_dim - 1)
    return x, y


def inc_surrounding(grid, x, y):
    print(x, y)
    y_dim, x_dim = len(grid), len(grid[0])
    for j in range(-1, 2):
        for i in range(-1, 2):
            if 0 <= y + j < y_dim and 0 <= x + i < x_dim:
                if grid[y + j][x + i] == None:
                    grid[y + j][x + i] = 1
                elif grid[y + j][x + i] != 0:
                    grid[y + j][x + i] += 1
    return grid


def place_bombs(grid, number_of_bombs):
    y_dim, x_dim = len(grid), len(grid[0])
    for i in range(number_of_bombs):
        while True:
            x, y = generate_coordinate(x_dim, y_dim)
            if grid[y][x] == None:
                grid[y][x] = 0
                grid = inc_surrounding(grid, x, y)
                break
    return grid


def print_grid(grid):
    # ▒▒
    for row in grid:
        result = ""
        for cell in row:
            char = "▒▒" if cell == None else "{:>2}".format(cell)
            result += char
        print(result)


def create_grid(dim):
    grid = []
    for j in range(dim):
        grid.append([None] * dim)
    return grid


def main(dim, num_bombs):
    """
    Main function called when script is run from the command line
    """
    print("in main function")
    print("{0} x {0} | number of bombs = {1}".format(dim, num_bombs))
    grid = create_grid(dim)

    grid = place_bombs(grid, num_bombs)

    print_grid(grid)


if __name__ == "__main__":
    dim, num_bombs = [int(x) for x in sys.argv[1:3]]
    main(dim, num_bombs)
