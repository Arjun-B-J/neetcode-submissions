class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a)-1
        j = len(b)-1
        res = []
        carry = 0 
        while i>=0 and j>=0:
            sums = int(a[i])+int(b[j])+carry  
            if sums==3:
                res.append('1')
                carry=1
            elif sums==2:
                res.append('0')
                carry=1
            else:
                res.append(str(sums))
                carry=0
            i-=1
            j-=1
        while i>=0:
            if carry and a[i]=='0':
                carry =0
                res.append('1')
                i-=1
                continue
            if carry and a[i]=='1':
                res.append('0')
                i-=1
                continue
            res.append(a[i])
            i-=1
        while j>=0:
            if carry and b[j]=='0':
                carry =0
                res.append('1')
                j-=1
                continue
            if carry and b[j]=='1':
                res.append('0')
                j-=1
                continue
            res.append(b[j])
            j-=1
        if carry:
            res.append('1')
        return "".join(res)[::-1]
