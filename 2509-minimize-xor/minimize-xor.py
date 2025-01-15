class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        
        totbits = 0
        while num2:
            totbits += (num2 % 2)
            num2 = num2 >> 1

        bits = []
        while num1:
            curr = num1 % 2
            bits.append(curr)
            num1 = num1 >> 1

        currbits = sum(bits)

        i = 0
        while i < len(bits) and currbits < totbits:
            while i < len(bits) and bits[i]:
                i += 1
            if i < len(bits):
                bits[i] = 1
                currbits += 1

        while currbits < totbits:
            bits.append(1)
            currbits += 1

        while i >= 0 and currbits > totbits:
            if bits[i]:
                bits[i] = 0
                currbits -=1
            i += 1    
        #  11001   65
        #  1001000   84 

        n = len(bits)
        ans = 0
        for i in range(n):
            val = bits[i]
            ans += (val << i)

        return ans
