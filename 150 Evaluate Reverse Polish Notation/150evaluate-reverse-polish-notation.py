class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def add(v1,v2):
            return v1 + v2
        def substract(v1,v2):
            return v1-v2
        def multiply(v1,v2):
            return v1*v2
        def divide(v1,v2):
            return int(v1/v2)

        operations = {
            "+": add,
            "-": substract,
            "*": multiply,
            "/": divide
        }

        n = len(tokens)
        stack = []
        for r in range(n):
            if tokens[r] in {"*","/","+","-"}:
                val2 = stack.pop()
                val1 = stack.pop()
                curr = operations[tokens[r]](val1, val2)
                stack.append(curr)
            else:
                stack.append(int(tokens[r]))
               

        return stack[-1]