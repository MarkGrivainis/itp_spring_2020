import pprint
numbers = [0,1,1,3,1,3,6,1,8,2,8,7,5,0,2,2,1,5,4,7,0,0,3,1,2,9,9,4,
           3,2,5,3,1,2,1,3,3,2,2,4,5,1,6,7,9,8,1,4,2,5,6,8,0,0,0,1,
           1,2,6,1,3,2,4,2,5,7,3,1,3,4,6]

## Solution 1
# counts = {}
# for num in numbers:
#     if num in counts:
#         counts[num] = counts[num] + 1
#     else:
#         counts[num] = 1
# pp = pprint.PrettyPrinter(width=10)
# pp.pprint(counts)


## Solution 2
# counts = {}
# for num in numbers:
#     counts[num] = counts.get(num, 0) + 1
# pp = pprint.PrettyPrinter(width=10)
# pp.pprint(counts)

# help(dict.get)


## Solution 3
# from collections import defaultdict
# counts = defaultdict(int)
# for num in numbers:
#     counts[num] += 1
# pp = pprint.PrettyPrinter(width=10)
# pp.pprint(counts)


## Solution 4
from collections import Counter
counter = Counter(numbers)

# help(counter) or help(Counter)
# some additional utilities that the Counter object provides...