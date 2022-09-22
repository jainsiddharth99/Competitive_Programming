class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dt = {v: k for k, v in enumerate(s)}
        st = []
        for k, v in enumerate(s):
            if v not in st:
                while st and st[-1] > v and dt[st[-1]] > k:
                    st.pop()

                st.append(v)

        return "".join(st)
