class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        mapping = {}
        stack = []
        results = []
        
        for num in nums2:
            while stack and num >  stack[-1]:
                val = stack.pop()
                mapping[val] = num
            stack.append(num)
                
        for i in range(len(stack)):
            mapping[stack[i]] = -1
                
        
        for num in nums1:
            results.append(mapping[num])
                
        return results
                        
                    
        