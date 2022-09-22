import math

"""
this one is not working for some test cases
def calculate(s: str) -> int:
    s = s.replace(" ", "")
    s = '('+s+')'
    st = []
    op = []
    curr = ''
    for i in s:
        if i == '(':
            st.append(i)
        elif i.isdigit():
            curr += i
        elif i in '+-':
            if curr:
                st.append(int(curr))
                curr = ""
            op.append(i)
        elif i == ')':
            if curr:
                st.append(int(curr))
                curr = ""
            top = st.pop()
            ans = 0
            while top != '(':
                r = top
                l = st.pop()
                if l == '(':
                    st.append(top)
                    break
                if op:
                    t = op.pop()

                    if t == '+':
                        ans = r+l
                    elif t == '-':
                        ans = l-r
                    st.append(ans)

                top = st.pop()
    return st.pop()
"""


def calculate(s: str) -> int:
    s = s.replace(" ", "")
    s += '+'
    st = [1]
    res = 0
    num = 0
    op = 1
    for i in s:
        if i.isdigit():
            num = (num*10)+int(i)
        elif i in '+-':
            res += num*op*st[-1]
            op = 1 if i == '+' else -1
            num = 0
        elif i == '(':
            st.append(st[-1]*op)
            op = 1
        elif i == ')':
            res += num*op*st[-1]
            num = 0
            st.pop()

    return res


s = " 2-1 + 2 "
print(calculate(s))
"""
Example 1:

Input: s = "1 + 1"
Output: 2

Example 2:

Input: s = " 2-1 + 2 "
Output: 3

Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

"""
