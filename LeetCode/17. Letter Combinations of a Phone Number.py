class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dt = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
              '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = ['']
        n = len(digits)
        if n == 0:
            return []
        elif n == 1:
            return dt[digits[0]]
        for i in digits:
            res = [p+q for p in res for q in dt[i]]
        return res
