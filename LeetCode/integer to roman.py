I=1
V=5
X=10
L=50
C=100
D=500
M=1000
def intToRoman(num):
    if num>=1:
        print('I'*num)
    elif num<=5 and num>=4:
        print('V')