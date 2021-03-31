import bisect
def maxEnvelopes(envelopes):
    # envelopes=sorted(envelopes, key=lambda x:(x[0],-x[1]))
    # ans=[]
    # ans.append(envelopes[0])
    # for i in range(len(envelopes)):
    #     for j in range(i+1,len(envelopes)):
    #         if ans[-1][0]< envelopes[j][0] and ans[-1][1]< envelopes[j][1]:
    #             ans.append(envelopes[j])
    # return len(ans)
    
    envelopes=sorted(envelopes, key=lambda x:(x[0],-x[1]))
    ans=[]
    for w,h in envelopes:
        index=bisect.bisect_left(ans,h)
        if index<len(ans):
            ans[index]=h
        else:
            ans.append(h)
            print(ans)
    return len(ans)
            
env=[[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
print(maxEnvelopes(env))