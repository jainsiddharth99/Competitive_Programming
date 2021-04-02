def myAtoi(s):
        s=s.strip()
        if s[0]=='-':
            num=""
            for i in s:
                if i=='.':
                    break
                if i.isdigit():
                    num+=i
            
            s='-',num
            s=''.join(s)
            s=int(s)
            return s if s>=-(2**31) else -(2**31)
        elif s[1].isalpha():
            s=0
            return s
        else:
            num=""
            for i in s:
                if i.isdigit():
                    num+=i
            s=int(num)
            return s if s<=(2**31-1) else 2**31
s='3.14'
print(myAtoi(s))