class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:

        def find(group,arr):
            for i in range(len(arr)):
                if group[0] == arr[i]:
                    for j in range(1,len(group)):
                        if i+j >= len(arr):
                            return -1
                        if group[j] != arr[i+j]:
                            break
                    else:
                        return i

            return -1


        l = 0
        for group in groups:
            res = find(group,nums[l:])
            if res == -1:
                return False
            l = res + len(group)

        return True

        