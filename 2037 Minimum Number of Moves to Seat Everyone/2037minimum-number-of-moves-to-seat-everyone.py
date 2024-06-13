class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

        seats.sort()
        students.sort()
        ans = 0
        for a,b in zip(seats,students):
            ans += abs(a-b)

        return ans
        