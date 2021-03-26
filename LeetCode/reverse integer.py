import numpy as np
def reverse(x):
    if x>0:
        num=str(x)
        x=num[::-1]
        x=int(x)
        
    else:
        num=str(-x)
        val= '-',num[::-1]
        x=''.join(val)
        x=int(x)
        
    return x if x<=(2**31-1) and x>=-(2**31) else 0
        
    
x=1534236469
print(reverse(x))