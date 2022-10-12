from collections import defaultdict, Counter


def topKFrequent(nums: list[int], k: int) -> list[int]:
    dt = defaultdict(int)
    for i in nums:
        dt[i] += 1

    x = dict(sorted(dt.items(), key=lambda x: x[1], reverse=True))
    res = []
    for key in x.keys():
        res.append(key)
    return res[:k]


def topKFrequent1(nums: list[int], k: int) -> list[int]:
    return [k for k, v in Counter(nums).most_common(k)]


def topKFrequent2(nums: list[int], k: int) -> list[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


nums = [1, 1, 1, 2, 2, 5, 5, 3]


print(topKFrequent2(nums, 2))


"""
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 
"""
