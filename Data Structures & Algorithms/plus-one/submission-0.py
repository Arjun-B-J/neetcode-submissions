class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in reversed(range(len(digits))):
            total = digits[i] + carry
            digits[i]=total%10
            carry = total//10
        if carry:
            digits.insert(0,carry)
        return digits