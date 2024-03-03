from sortedcontainers import SortedList
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
                            
        n = len(nums)
        arr1 = SortedList()
        arr2 = SortedList()
        arr1.add(nums[0])
        arr2.add(nums[1])
        
        list1 = [nums[0]]
        list2 = [nums[1]]

        
        for i in range(2,n):
            num = nums[i]
            val1 = arr1.bisect_left(num+1)
            val1 = len(arr1) - val1
            val2 = arr2.bisect_left(num+1)
            val2 = len(arr2) - val2
            # print(val1,val2)
            
            if val1 > val2:
                arr1.add(num)
                list1.append(num)
            elif val1 < val2:
                arr2.add(num)
                list2.append(num)
            else:
                if len(arr1) <= len(arr2):
                    arr1.add(num)
                    list1.append(num)
                else:
                    arr2.add(num)
                    list2.append(num)
            # print("list")
            # print(list1,list2)
                    
                
            
        return list1 + list2