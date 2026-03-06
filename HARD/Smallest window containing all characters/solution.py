import math
from collections import Counter
class Solution:
    def minWindow(self, s, p):
        n1=len(s)
        n2=len(p)
        
        if n1<n2:
            return ""
            
        left=0
        right=0
        res=""
        mini=math.inf
        d1=dict()
        d2=Counter(p)
        
        have=0
        
        while (right<n1):
            ch=s[right]
            
            if ch in d2:
                d2[ch]-=1
            
                if d2[ch]>=0:
                    have+=1
        
            while (have==n2 and left<n1):
                if mini>(right-left+1):
                    mini=(right-left+1)
                    res=s[left:right+1]
                
                if s[left] in d2:
                    d2[s[left]]+=1
                
                    if d2[s[left]]>0:
                        have-=1
                        
                left+=1
            
            right+=1
        
        return res
