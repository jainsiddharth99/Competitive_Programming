def halvesAreAlike(s):
        div=int(len(s)/2)
        a=s[:div]
        b=s[div:]
        vowels=['a','e','i','o','u','A','E','I','O','U']
        alist=[]
        blist=[]
        for i in a:
            for vowel in vowels:
                if vowel==i:
                    alist.append(vowel)
        for j in b:
            for vowel in vowels:
                if vowel==j:
                    blist.append(vowel)
        return bool(len(alist)==len(blist))
    
s='abcdefgh'
print(halvesAreAlike(s))