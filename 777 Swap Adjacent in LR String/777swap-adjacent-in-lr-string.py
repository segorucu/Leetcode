class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        
        one = []
        two = []
        for i,(a,b) in enumerate(zip(start,result)):
            if a in {"R","L"}:
                one.append((a,i))
            if b in {"R","L"}:
                two.append((b,i))

        if len(one) != len(two):
            return False
        
        for (s,s_i),(e,e_i) in zip(one,two):
            if s != e:
                return False
            if s == "L":
                if s_i < e_i:
                    return False
            if s == "R":
                if s_i > e_i:
                    return False


        return True