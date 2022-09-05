def evalRPN(tokens: list[str]) -> int:
    s = []
    for i in tokens:
        if i not in '+-*/':
            s.append(int(i))

        else:
            r, l = s.pop(), s.pop()
            if i == '+':
                s.append(l+r)
            elif i == '-':
                s.append(l-r)
            elif i == '*':
                s.append(l*r)
            else:
                s.append(int(float(l)/r))

    return s.pop()


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(evalRPN(tokens))

"""
Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""
