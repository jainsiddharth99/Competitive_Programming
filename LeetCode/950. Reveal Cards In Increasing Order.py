from collections import deque


def deckRevealedIncreasing(deck: list[int]) -> list[int]:
    q = deque()
    for i in sorted(deck)[::-1]:
        if q:
            q.appendleft(q.pop())
        q.appendleft(i)
    return q


deck = [17, 13, 11, 2, 3, 5, 7]
print(deckRevealedIncreasing(deck))
