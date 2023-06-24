class Solution:
    def simplifyPath(self, path: str) -> str:
        
        dirs = path.split("/")
        stack = []
        for d in dirs:
            if len(d) == 0:
                continue
            elif d == ".":
                continue
            elif d == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(d)
            
                    
                        
          
        return "/"+"/".join(stack)