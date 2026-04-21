class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        res = [0] *(len(num1)+len(num2))

        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                carryIdx = i+j
                digitIdx = i+j+1

                totalSum = res[digitIdx]+(int(num1[i])*int(num2[j]))
                res[digitIdx] = totalSum%10
                res[carryIdx] = res[carryIdx]+totalSum//10
        
        for i in range(len(res)):
            if res[i]!=0:
                break
        
        return "".join(map(str,res[i:]))

