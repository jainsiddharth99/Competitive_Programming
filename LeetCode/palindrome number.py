def isPalindrome(x):
        x=str(x)
        return (bool(x==x[::-1]))

x=101
if isPalindrome(x):
    print ('true')
else:
    print ('false')
