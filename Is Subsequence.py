class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k=True
        newlist=[]
        idx = 0
        for a in t :
            newlist.append(a)
        for a in range(idx,len(newlist)):
            if s[a] in newlist:
                idx = 
            else:
                k=False
        return k 
