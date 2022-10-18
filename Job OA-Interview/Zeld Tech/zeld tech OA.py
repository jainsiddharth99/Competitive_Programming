def solution(A):
    # write your code in Python 3.6
    res = 0
    if cutting(A):
        return 0

    for i in range(len(A)):
        s = A[:i]+A[i+1:]
        if cutting(s):
            res += 1
    return res if res != 0 else -1


def cutting(A):
    for i in range(1, len(A)-1):
        if (A[i-1] <= A[i] <= A[i+1]) or (A[i-1] >= A[i] >= A[i+1]):
            return False
    return True


A = [3, 4, 5, 3, 7]

print(solution(A))
