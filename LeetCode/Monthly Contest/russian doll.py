def maxEnvelopes(envelopes):
    envelopes=sorted(envelopes)
    # print(envelopes)
    ans=[]
    for i in range(len(envelopes)):
        ans.append(envelopes[0])
        for j in range(i+1,len(envelopes)):
            if ans[-1][0]< envelopes[j][0] and ans[-1][1]< envelopes[j][1]:
                ans.append(envelopes[j])
        return ans
            
env=[[5,4],[6,4],[6,7],[2,3]]
print(maxEnvelopes(env))