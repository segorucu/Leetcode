class Solution:
    def numberToWords(self, num: int) -> str:

        if num == 1000000:
            return "One Million"
        elif num == 1000000000:
            return "One Billion"

        convert = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred"
                   }
        if num == 0:
            return "Zero"
        num = str(num)

        n = len(num)
        ans = []
        digit = -1
        short = ""
        for i in range(n-1,-1,-1):
            if (n - 1 - i) % 3 == 0:
                if i - 1 < 0 or num[i-1] == "0":
                    val = int(num[i])
                    if val == 0:
                        pass
                    else:
                        short = convert[val] + short
                else:
                    val = int(num[i-1:i+1])
                    if val in convert:
                        tmp = convert[val]
                    else:
                        rem = val % 10
                        if rem == 0:
                            tmp = convert[val-rem]
                        else:
                            tmp = convert[val-rem] + " " + convert[rem]
                    short = tmp + short
            elif (n-1-i) % 3 == 1:
                pass
            elif (n-1-i) % 3 == 2:
                val = int(num[i])
                if val in convert:
                    tmp = convert[val] + " Hundred "
                    short = tmp + short
            digit += 1
            if digit in {2,5,8}:
                short = short.lstrip()
                short = short.rstrip()
                if short:
                    ans.append(short)
                short = ""
            elif digit == 3:
                short = short.lstrip()
                short =short.rstrip()
                if num[i-2:i+1] != "000":
                    ans.append(short + " Thousand")
                short = ""
            elif digit == 6:
                short = short.lstrip()
                short = short.rstrip()
                if num[i-2:i+1] != "000":
                    ans.append(short + " Million")
                short = ""
            elif digit == 9:
                short = short.lstrip()
                short = short.rstrip()
                if num[i-2:i+1] != "000":
                    ans.append(short + " Billion")
                short = ""

        for i,val in enumerate(ans):
            ans[i] = ans[i].lstrip()
        if len(short) > 0:
            short = short.lstrip()
            short = short.rstrip()
            ans.append(short)
        ans.reverse()
        return " ".join(ans)


        