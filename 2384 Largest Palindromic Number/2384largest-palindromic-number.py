class Solution:
    def largestPalindromic(self, num: str) -> str:
        tab = collections.Counter(num)
        ans = ""
        single = False
        sorted_keys = sorted(tab.keys(),reverse=True)
        singlenum = None
        for key in sorted_keys:
            val = tab[key]
            if key == "0":
                continue
            div = (val // 2)
            if div > 0:
                ans += key * div
            if val % 2 == 1:
                single = True
                if singlenum is None:
                    singlenum = key
                elif key > singlenum:
                    singlenum = key
        if not single:
            if len(ans) == 0:
                return "0"
            return ans + "0" * tab["0"] + ans[::-1]

        else:
            div = tab["0"] // 2
            if div > 0 and len(ans) >= 1:
                ans += "0" * div
            return ans + singlenum + ans[::-1]
            