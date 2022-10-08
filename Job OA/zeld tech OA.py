def solution(A):
    # write your code in Python 3.6
    res = 0
    if cutting(A):
        return 0

    for i in range(len(A)):
        s = sub(A, 0, len(A)-1)
        s = s[:i]+s[i+1:]
        if cutting(s):
            res += 1
    return res if res != 0 else -1


def sub(A, start, end):
    lt = []
    for i in range(start, end+1):
        lt.append(A[i])
    return lt


def cutting(A):
    for i in range(1, len(A)-1):
        if (A[i-1] <= A[i] and A[i] <= A[i+1]) or (A[i-1] >= A[i] and A[i] >= A[i+1]):
            return False
    return True


A = [3, 4, 5, 3, 7]

print(solution(A))
