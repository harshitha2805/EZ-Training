'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        res=[]
        h=1
        if len(s)==0:
            return 0
        for i in range(len(s)):
            res.append(s[i])
            c=1
            j=i+1
            while j<len(s): 
                if s[j] not in res:
                    c+=1 
                    res.append(s[j])
                    l=len(res)
                    j+=1
                else:
                    res=[]   
                    break 
                if h<c:
                    h=c
        return h
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        l,lngSubstr=0,0
        sw=set()
        for r in range(len(s)):
            while s[r] in sw:
               sw.remove(s[l])
               l+=1
            sw.add(s[r])
            lngSubstr=max(lngSubstr,(r-l+1))
        return lngSubstr