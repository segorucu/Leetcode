class Solution:
    operations = {
            "-": lambda x, y : x - y,
            "+": lambda x, y : x + y,
            "*": lambda x, y : x * y,
        }

    @cache
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        if expression.isnumeric():
            return [int(expression)]

        res = []
        for i in range(len(expression)):
            op = expression[i]
            if op in self.operations:
                nums1 = self.diffWaysToCompute(expression[:i])
                nums2 = self.diffWaysToCompute(expression[i+1:])

                for num1 in nums1:
                    for num2 in nums2:
                        val = self.operations[op](num1,num2)
                        res.append(val)
        return res

        