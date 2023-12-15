class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        origin = set()
        for orig, dest in paths:
            origin.add(orig)

        for orig, dest in paths:
            if dest not in origin:
                return dest
