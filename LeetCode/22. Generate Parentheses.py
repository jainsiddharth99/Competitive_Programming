def generateParenthesis(n: int) -> list[str]:
    res = []
    s = []

    def backtrack(open, close):
        if open == close == n:
            res.append("".join(s))
        if open < n:
            s.append('(')
            backtrack(open+1, close)
            s.pop()
        if close < open:
            s.append(')')
            backtrack(open, close+1)
            s.pop()
    backtrack(0, 0)
    return res


print(generateParenthesis(3))
"""
Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 
"""
