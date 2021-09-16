# I=1
# V=5
# X=10
# L=50
# C=100
# D=500
# M=1000
def intToRoman(num):
    if num>=1 and num<=3:
        print('I'*num)
    elif num<5:
        print('IV')
    elif num==5:
        print('V')
    elif num>5 and num<=8:
        print ('V'+'I'*(num-5))
    elif num==10:
        print('X')
    elif num==50:
        print('L')
    elif num==100:
        print('C')
    elif num==500:
        print('D')
    elif num==1000:
        print('M')
        
num=8
intToRoman(num)
        