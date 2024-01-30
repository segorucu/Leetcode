class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        counter = collections.Counter(nums)
        
        ans = 1
        if counter[1] > 1:
            if counter[1] % 2 == 1:
                ans = counter[1]
            else:
                ans = counter[1]-1
        
        visited = set()
        for node in counter.keys():
            if node in visited or node == 1:
                continue
            visited.add(node)
            parent = node
            tmp = 1
            while parent:
                child = math.sqrt(parent)
                if not child.is_integer():
                    break
                child = int(child)
                if counter[child] > 1:
                    tmp += 2
                    parent = child
                    ans = max(ans,tmp)
                    visited.add(child)
                else: 
                    break
                      
        return ans