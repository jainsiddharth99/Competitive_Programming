def isPalindrome(x):
    x=str(x)
    print(x)
    x=x.replace(',','')
    print(x)
    x=x.replace(' ','')
    print(x[1:-1])
    print(x[-2:0:-1])
    return (bool(x[1:-1]==x[-2:0:-1]))

x=[1,2,2,1]
if isPalindrome(x):
    print ('true')
else:
    print ('false')
