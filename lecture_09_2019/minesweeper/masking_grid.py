"""
DOC STINGR

DESC
"""
import sys


def set_true(mask, x, y):
    if 0 <= x < len(mask[0]) and 0 <= y < len(mask):
        mask[y][x] = True
    return mask


def generate_mask(dim):
    # mask = [[False for x in range(dim)]for y in range(dim)]
    mask = []
    for y in range(dim):
        tmp = []
        for x in range(dim):
            tmp.append(False)
        mask.append(tmp)
    return mask


def print_mask(mask):
    for row in mask:
        print(row)
    print()


def main(dim):
    mask = generate_mask(dim)
    print(mask)
    print()
    print(mask[0])
    # print_mask(mask)
    # set_true(mask, 0, 0)
    # set_true(mask, dim - 1, dim - 1)
    # print_mask(mask)


if __name__ == "__main__":
    dim = int(sys.argv[1])
    main(dim)
