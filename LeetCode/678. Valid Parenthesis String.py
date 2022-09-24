def checkValidString(s: str) -> bool:
    bracket = []
    star = []
    for i in range(len(s)):
        if s[i] == '(':
            bracket.append(i)

        elif s[i] == '*':
            star.append(i)

        else:
            if bracket:
                bracket.pop()

            elif star:
                star.pop()
            else:
                return False

    while bracket and star:
        if star[-1] < bracket[-1]:
            return False
        bracket.pop()
        star.pop()

    return not bracket
