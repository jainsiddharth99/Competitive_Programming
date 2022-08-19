class Solution:
    def isValid(self, s: str) -> bool:
        dic={'(':')','[':']','{':'}'}
        lt=[]
        for i in s:
            if i in dic:
                lt.append(dic[i])
            else:
                if len(lt)>0 and lt[-1]==i:
                    lt.pop()
                else:
                    return False
        return len(lt)==0
        