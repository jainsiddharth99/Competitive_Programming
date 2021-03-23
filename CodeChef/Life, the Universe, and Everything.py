def number():
    n=int(input())
    if n<100 and n!=42:
        print(n)
        return number()
number()