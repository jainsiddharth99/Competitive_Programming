class Solution:
    def reverseVowels(self, s: str) -> str:
        s = [i for i in s]
        i = 0
        j = len(s)-1
        while i < j:
            if s[i].lower() in ['a', 'e', 'i', 'o', 'u'] and s[j].lower() in ['a', 'e', 'i', 'o', 'u']:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

            elif s[i].lower() in ['a', 'e', 'i', 'o', 'u']:
                j -= 1
            else:
                i += 1
        return "".join(s)
