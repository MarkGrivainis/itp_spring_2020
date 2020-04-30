import sys
from file_handling import read_complete_file
from stats import (
    count_number_of_lines,
    count_number_of_words,
    get_word_counts,
    get_top_words,
)


# number of lines in the file
# number of words
# number of characters


def main(filepath):
    data = read_complete_file(filepath)
    num_lines = count_number_of_lines(data)
    print(num_lines)
    num_words = count_number_of_words(data)
    print(num_words)
    counts = get_word_counts(data)
    print(get_top_words(counts))


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 1:
        main(args[0])
    else:
        print("too many/few args, should just be the file path")
