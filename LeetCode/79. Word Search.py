from collections import Counter
from itertools import chain


def exist(board, word):
    res = dict(Counter(chain(*board)))

    b = Counter(word)

    for k, v in b.items():
        if res[k] < v:
            return False
    return True


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(exist(board, word))
