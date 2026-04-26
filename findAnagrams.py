class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s=list(s)
        p=list(p)
        p.sort()
        (s1,s2)=(len(s), len(p))
        l=[]

        for i in range (s1):
            f=s[i:i+s2]
            f.sort()
            if f==p:
                l.append(i)
            if i+s2>s1:
                break
            
        return (l)
