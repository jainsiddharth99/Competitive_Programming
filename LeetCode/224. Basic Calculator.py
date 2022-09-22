import math


def calculate(s: str) -> int:
    s = s.replace(" ", "")
    s += '+'
    st = []
    num = 0
    op = '+'
    # num = ''
    for i in s:
        if i.isdigit():
            num = (num*10)+int(i)
            # num += i
        else:
            num = int(num)
            if op == '+':
                st.append(num)
            elif op == '-':
                st.append(-num)
            elif op == '*':
                st.append(st.pop()*num)
            elif op == '/':
                st.append(int(st.pop()/num))
            # num = ''
            num = 0
            op = i
    return sum(st)


s = "14-3/2"
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
