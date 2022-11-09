class Solution:
    def maximum69Number(self, num: int) -> int:
        s = [i for i in str(num)]
        for i in range(len(s)):
            if s[i] == '6':
                s[i] = '9'
                print(s)
                break
        return int(''.join(s))
