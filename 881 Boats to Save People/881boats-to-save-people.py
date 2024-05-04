# from collections import Counter
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()

        boats = 0
        left = 0
        right = len(people) - 1
        while right >= left:
            boats += 1
            if people[right] + people[left] <= limit:
                left += 1  
            right -= 1

        return boats
