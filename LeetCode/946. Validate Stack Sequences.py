def validateStackSequences(pushed: list[int], popped: list[int]) -> bool:
    s = []
    popped = popped[::-1]
    for i in pushed:
        s.append(i)
        while s and s[-1] == popped[-1]:
            s.pop()
            popped.pop()
    return len(s) == 0


pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]
print(validateStackSequences(pushed, popped))
"""
Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
"""
