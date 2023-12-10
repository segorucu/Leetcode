class Solution:
    def intToRoman(self, num: int) -> str:
        tab = {
            1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
            40: "XL", 50: "L", 90: "XC", 100: "C",
            400: "CD", 500: "D", 900: "CM", 1000: "M"
        }

        numbers = list(tab.keys())
        pointer = len(numbers)-1
        ans = []
        while num > 0:
            dum = num // numbers[pointer]
            while dum == 0:
                pointer -= 1
                dum = num // numbers[pointer]
            num = num % numbers[pointer]
            ans.append(dum * tab[numbers[pointer]])

        return ''.join(ans)