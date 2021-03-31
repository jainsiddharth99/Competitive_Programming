def maxEnvelopes(envelopes):
    envelopes=sorted(envelopes)
    print(envelopes)
    ans=[]
    for envelope in envelopes:
        print(envelope)
        for i in range(1,len(envelope),2):
            # print(i)
            print(envelopes[i])
            
env=[[5,4],[6,4],[6,7],[2,3]]
print(maxEnvelopes(env))