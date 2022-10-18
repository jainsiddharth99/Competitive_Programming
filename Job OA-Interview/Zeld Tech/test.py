# ar = [89, 356, 9, 90, 353]
# # 9,90,89,356,353
# ar.sort()
# print(str(ar[1-1:]))
# print(str(ar[1])+str(ar[1-1])+str(ar[1+1:]))


import functools

ar = [89, 356, 9, 90, 353]


def compare(x, y):
    xy = int(str(x)+str(y))
    yx = int(str(y)+str(x))
    return yx-xy


ar.sort(key=functools.cmp_to_key(compare))

print(ar)

# # ar=[9,89,90,353,356]
# for i in range(1,len(ar)):
#     left=str(ar[i-1:])
#     right=str(ar[i])+str(ar[i-1])+str(ar[i+1:])


# print(ar.sort(key=lambda x,y: x-y))


# def compare(ar):
#     for i in range(1,len(ar)):
#         x=ar[i-1]
#         y=ar[i]

#     return x-y


# a = sorted(ar, cmp=lambda x, y: x-y)
# print(a)
