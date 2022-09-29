def minAddToMakeValid(s: str) -> int:
    st = []
    c = 0
    for i in s:
        if i == '(':
            st.append(1)
        elif st and i == ')':
            st.pop()
        else:
            c += 1
    return sum(st) + c


s = "()))"
print(minAddToMakeValid(s))
