def sumSubarrayMins(arr: list[int]) -> int:
    n = len(arr)
    res = [0]*n
    s = []
    lar = []
    for i in range(n):
        while s and arr[s[-1]] > arr[i]:
            s.pop()
        if s:
            lar.append(s[-1])
        else:
            lar.append(-1)
        s.append(i)

    for i in range(n):
        j = lar[i]
        if j == -1:
            res[i] = (i+1)*arr[i]
        else:
            res[i] = res[j]+(i-j)*arr[i]
    return sum(res) % (10**9+7)


arr = [3, 1, 2, 4]
print(sumSubarrayMins(arr))


"""
Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444
"""
