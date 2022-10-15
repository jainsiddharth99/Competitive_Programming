def solution(nums):
    res = set()
    curr = 0
    i = 0
    for j in range(0, len(nums)):
        curr += nums[j]
        if curr >= 0:
            res.add(curr)
        else:
            while curr < 0:
                curr -= nums[i]
                i += 1
    return sum(res)


t = int(input())
res = []
for i in range(t):
    N = int(input())
    lt = list(map(int, input().split()))
    a = solution(lt)
    res.append(a)
for i in range(len(res)):
    print('Case #{}:'.format(i+1), res[i])
