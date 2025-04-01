class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        # if num[0] == "0": return []

        n= len(num)
        # num = [int(v) for v in num]
        options = ["+","-","*"]

        def evaluate(operands, operators):
            stack = [int(operands[0])]
            opstack = []
            for val, op in zip(operands[1:],operators):
                if op == "*":
                    stack.append(stack.pop()*int(val))
                else:
                    stack.append(int(val))
                    opstack.append(op)

            sm = stack[0]
            for val, op in zip(stack[1:], opstack):
                if op == "-":
                    sm -= val
                else:
                    sm += val

            return sm

        def convert(num, curr):
            arr = [num[0]]
            for a,b in zip(num[1:], curr):
                arr.append(b)
                arr.append(a)
            return "".join(arr)



        # sm = evaluate(num, ["-","-"])
        # print(sm)
        ans = []
        curr = []
        numstack = [num[0]]
        def permute(i):
            if i == n:
                if evaluate(numstack, curr) == target:
                    txt = convert(numstack, curr)
                    ans.append(txt)
                return

            for option in options:
                curr.append(option)
                numstack.append(num[i])
                permute(i+1)
                curr.pop()
                numstack.pop()

            if int(numstack[-1]) != 0:
                tmp = numstack.pop()
                numstack.append(tmp+num[i])
                permute(i+1)
                numstack.pop()
                numstack.append(tmp)

        permute(1)

        return ans

            
