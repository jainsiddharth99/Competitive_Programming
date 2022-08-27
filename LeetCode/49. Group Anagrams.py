from collections import defaultdict


def groupAnagrams(strs):
    # edge cases
    # res = {}
    res = defaultdict(list)
    for i in strs:
        res["".join(sorted(i))].append(i)

    return res.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
