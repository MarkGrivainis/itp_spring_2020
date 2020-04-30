from collections import defaultdict


def count_number_of_lines(text):
    # return len(text.split("\n"))
    return text.count("\n") + 1


def count_number_of_words(text):
    return len(text.split(" "))


def get_word_counts(text):
    word_counts = defaultdict(int)
    for word in text.split():
        word_counts[word] += 1
    return word_counts


def get_top_words(word_count_dict, n=10):
    return sorted(
        word_count_dict.items(), key=lambda x: (x[1], len(x[0])), reverse=False
    )[:n]
