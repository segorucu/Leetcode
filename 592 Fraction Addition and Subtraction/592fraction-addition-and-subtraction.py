class Solution:
    def fractionAddition(self, expression: str) -> str:
        
        signlst = []
        nominator = []
        denominator = []

        n = len(expression)
        l = 0
        while l < n:
            if len(signlst) == 0 and expression[l] != "-":
                signlst.append("+")
            if expression[l] == "-":
                signlst.append("-")
            elif expression[l] == "+":
                signlst.append("+")
            elif expression[l] == "/":
                pass
            else:
                num = ""
                while l < n and expression[l] not in {"-","+","/"}:
                    num += expression[l]
                    l += 1
                l -= 1
                if len(nominator) == len(denominator):
                    nominator.append(int(num))
                else:
                    denominator.append(int(num))
            l += 1

        temp = set(denominator)
        commonden = 1
        for val in temp:
            commonden *= val

        sm = 0
        for i in range(len(signlst)):
            add = commonden // denominator[i] * nominator[i]
            if signlst[i] == "+":
                sm += add
            else:
                sm -= add

        if sm < 0:
            sgn = "-"
        else:
            sgn = ""
        sm = abs(sm)
        for i in range(2,min(commonden,sm)+1):
            while sm % i == 0 and commonden % i == 0:
                sm = sm // i
                commonden = commonden // i

        if sm == 0:
            commonden = 1

        return sgn + str(sm) + "/" + str(commonden)
