class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []
        self.ans = []
        self.find_ip('', s, 4)
        return self.ans

    def find_ip(self, prev_ans, remain_s, remain_choice):
        if remain_choice == 0 and remain_s == '':
            self.ans.append(prev_ans[:-1])
            return
        if remain_choice == 0:
            return
        for i in range(1, 4):
            if len(remain_s) >= i:
                if self.is_valid(remain_s[:i]):
                    self.find_ip(prev_ans + remain_s[:i] + '.', remain_s[i:],
                                 remain_choice - 1)

    def is_valid(self, s):
        if len(s) == 1:
            return True
        if len(s) == 2 and s[0] != '0':
            return True
        if len(s) == 3 and s[0] != '0' and int(s) <= 255:
            return True
        return False
