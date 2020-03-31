import grid
import masking_grid
import sys


def print_current_board(board, mask):
    grid.print_grid(board)
    for j, row in enumerate(mask):
        result = ""
        for i, col in enumerate(row):
            tmp_char = ""
            if not mask[j][i]:
                tmp_char = "X"
            else:
                tmp_cell = board[j][i]
                tmp_char = tmp_cell if tmp_cell != None else " "

            result += str(tmp_char)
        print(result)


def main(dim, num_bombs):
    # Initialize the game
    # Set up the mask
    # loop
    # print the grid
    # prompt for input()
    # x, y, operation
    # if not board:
    # intialize the board
    # update the grid
    board = grid.create_grid(dim)
    mask = masking_grid.generate_mask(dim)
    initialized = False

    while True:
        print_current_board(board, mask)
        inp = input('enter command (x, y, ["o", "f"]) or "x" to quit:\n')
        if inp == "x":
            break
        if not initialized:
            grid.place_bombs(board, num_bombs)
            initialized = True
        split_inp = inp.split()
        x, y = [int(i) for i in split_inp[0:2]]
        operator = split_inp[2]
        masking_grid.set_true(mask, x, y)


if __name__ == "__main__":
    dim, num_bombs = [int(x) for x in sys.argv[1:3]]
    main(dim, num_bombs)
