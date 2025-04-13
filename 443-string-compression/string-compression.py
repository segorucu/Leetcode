class Solution:
    def compress(self, chars: List[str]) -> int:
        

        s = []
        for k,v in groupby(chars):
            num = len(list(v))
            s.append(k)
            if 1 < num < 10:
                s.append(str(num))
            elif num >= 10:
                txt = str(num)
                for t in txt:
                    s.append(t)

        chars.clear()
        chars.extend(s)

        return len(chars)