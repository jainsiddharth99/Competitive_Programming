from collections import Counter, defaultdict


def topKFrequent1(words: list[str], k: int) -> list[str]:
    return [k for k, v in Counter(sorted(words)).most_common(k)]


def topKFrequent2(words: list[str], k: int) -> list[str]:
    dt = Counter(words)
    x = sorted(dt, key=lambda x: (-dt[x], x))
    return x[:k]
