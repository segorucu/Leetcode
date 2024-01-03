class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        sm = 0
        prev = 0
        for row in bank:
            curr = row.count("1")
            if curr > 0:
                sm += prev * curr
                prev = curr

        return sm
        