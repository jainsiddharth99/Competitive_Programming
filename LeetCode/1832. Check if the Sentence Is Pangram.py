from collections import Counter


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        cnt = Counter(sentence)
        if len(cnt) == 26:
            return True
        return False
