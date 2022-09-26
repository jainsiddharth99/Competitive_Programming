def maxChunksToSorted2(arr: list[int]) -> int:
    hi = arr[0]
    c = 0
    for i in range(len(arr)):
        hi = max(hi, arr[i])

        if hi == i:
            c += 1
    return c


def maxChunksToSorted2(arr: list[int]) -> int:
    s = []
    for i in arr:
        curr = i
        while s and s[-1] > i:
            curr = max(curr, s.pop())
        s.append(curr)
    return len(s)


arr = [2, 0, 1]
print(maxChunksToSorted2(arr))

"""


Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
Example 2:

Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
 """
