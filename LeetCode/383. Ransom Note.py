def canConstruct(ransomNote, magazine):
    randict = {}
    magdict = {}
    for i in ransomNote:
        if i not in randict:
            randict[i] = 1
        else:
            randict[i] += 1
    for j in magazine:
        if j not in magdict:
            magdict[j] = 1
        else:
            magdict[j] += 1

    for k, v in randict.items():
        if k not in magdict:
            return False
        if magdict[k] < v:
            return False

    return True


ransomNote = "a"
magazine = "b"
print(canConstruct(ransomNote, magazine))
