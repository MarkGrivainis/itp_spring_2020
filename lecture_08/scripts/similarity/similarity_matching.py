from pprint import pprint
from itertools import combinations


# 1. take in a sparse rating matrix and generate smaller matrices

# 2. compute pairwise similarity

def reverse_matrix(rating_matrix):
    # {user1: {i1: 2, i2: 3},
    # }
    # {item1: {u1: 5, u2: 5}
    # }
    pass

def compute_pairwise_dissimilarity(dict1, dict2):
    # 1. find common keys
    # 2. Abs difference in values of common keys
    # 3. Average abs diff

    # common = []
    # for key in dict1.keys():
    #     if key in dict2:
    #         common.append(key)

    common = set(dict1.keys()).intersection(set(dict2.keys()))

    abs_diff = 0
    for idx, key in enumerate(common):
        abs_diff += abs(dict1[key]-dict2[key])
    abs_avg = abs_diff/(idx+1)
    return abs_avg

def find_most_dissimilar_pair(rating_matrix):
    # 1. generate item pairs
    # 2. compute dissimilarity and save it
    # 3. sort the dissimilarities
    # 4. return the most similar / least dissimilar item pair

    def sort_key(item):
        return item[1]

    # pairs = []
    # keys = list(rating_matrix.keys())
    # for idx, key1 in enumerate(keys):
    #     for key2 in keys[idx+1: ]:
    #         pairs.append((key1, key2))

    #         user1   user2   user3   user4
    # user1    0,0    0,1     0,2     0,3
    # user2    1,0    1,1     1,2     1,3
    # user3    2,0    2,1     2,2     2,3
    # user4    3,0    3,1     3,2     3,3
    pairs = list(combinations(rating_matrix.keys(), 2))
    dissimilarity = []
    for user1, user2 in pairs:
        ratings1 = rating_matrix[user1]
        ratings2 = rating_matrix[user2]
        score = compute_pairwise_dissimilarity(ratings1, ratings2)
        dissimilarity.append([(user1, user2), score])
    pprint(dissimilarity)
    dissimilarity.sort(key=sort_key)
    pprint(dissimilarity)
    return dissimilarity[0]


if __name__ == '__main__':
    user_item_rating = {
        'user1': {'item1': 2.5, 'item2': 3.5, 'item3': 3.0,
                  'item4': 3.5, 'item5': 2.5, 'item6': 3.0},
        'user2': {'item1': 3.0, 'item2': 3.5, 'item3': 1.5,
                  'item4': 5.0, 'item5': 3.5, 'item6': 3.0},
        'user3': {'item1': 2.5, 'item2': 3.0, 'item4': 3.5,
                  'item6': 4.0},
        'user4': {'item2': 3.5, 'item3': 3.0, 'item4': 4.0,
                  'item5': 2.5, 'item6': 4.5},
        'user5': {'item1': 3.0, 'item2': 4.0, 'item3': 2.0,
                  'item4': 3.0, 'item5': 2.0, 'item6': 3.0},
        'user6': {'item1': 3.0, 'item2': 4.0, 'item4': 5.0,
                  'item5': 3.5, 'item6': 3.0},
        'user7': {'item2': 4.5, 'item4': 4.0, 'item5': 1.0}
    }

    most_dissimilar_user = find_most_dissimilar_pair(user_item_rating)
    print('most_dissimilar user pair: ', most_dissimilar_user)

    item_user_rating = reverse_matrix(user_item_rating)
    most_dissimilar_item = find_most_dissimilar_pair(item_user_rating)
    print('most_dissimilar item: ', most_dissimilar_item)

    # dict1 = user_item_rating['user1']
    # dict2 = user_item_rating['user2']
    # print(compute_pairwise_dissimilarity(dict1, dict2))
