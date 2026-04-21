# Time Complexity: O(M * N) - Where M and N are the lengths of the two strings.
# Space Complexity: O(M + N) - The maximum possible length of the product.
# Approach: Grade-School Multiplication Simulation

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Edge Case: If either number is zero, the product is zero.
        if num1 == "0" or num2 == "0":
            return "0"

        # The max length of a product of two numbers is the sum of their lengths
        # e.g., 99 * 99 = 9801 (2 digits + 2 digits = 4 digits)
        res = [0] * (len(num1) + len(num2))

        # Start multiplying from right to left (just like on paper)
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                
                # 1. Multiply the single digits
                mul = int(num1[i]) * int(num2[j])

                # 2. Determine the two positions in the result array
                # p1 is the "carry" position, p2 is the "current digit" position
                p1, p2 = i + j, i + j + 1

                # 3. Add our multiplication result to whatever is already at p2
                total_sum = mul + res[p2]

                # 4. Store the ones-place digit at p2
                res[p2] = total_sum % 10
                
                # 5. Add the tens-place carry to p1
                # (Use += because p1 might already have a value from a previous step!)
                res[p1] += total_sum // 10

        # The result array might have leading zeros (e.g., [0, 4, 0, 8]).
        # We need to find the first non-zero digit to skip them.
        ptr = 0
        while ptr < len(res) and res[ptr] == 0:
            ptr += 1

        # Convert the remaining integers back to strings and join them
        return "".join(map(str, res[ptr:]))