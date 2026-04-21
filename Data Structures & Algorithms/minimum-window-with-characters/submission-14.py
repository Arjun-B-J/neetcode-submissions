class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t)>len(s):
            return ""
        #get count
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c,0)    
        l = 0 #left pointer
        res,resLength = [-1,-1],float("inf")
        have,need = 0, len(countT)
        window = {}
        #plan is to get have == need then we decrement the window left side until its not met every time
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r],0)
            if s[r] in countT and countT[s[r]]==window[s[r]]:
                have+=1
            
            while have == need: #decrement the window, update if result 
                if (r-l+1) < resLength:
                    resLength = r-l+1
                    res = [l,r]
                window[s[l]]-=1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have-=1
                l+=1
        return s[res[0]:res[1]+1] if resLength!=float("inf") else ""


         