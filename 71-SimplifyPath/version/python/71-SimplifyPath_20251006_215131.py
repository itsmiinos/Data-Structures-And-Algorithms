# Last updated: 10/6/2025, 9:51:31 PM
class Solution:
    def simplifyPath(self, path: str) -> str:
        curr = ""
        stack = []

        for c in path + "/" :
            if c == "/" : 
                if curr == ".." : 
                    if len(stack) > 0 : 
                        stack.pop(-1)
                
                elif curr != "." and curr != "": 
                    stack.append(curr)
                curr = ""
            
            else : 
                curr += c
        
        return "/" + "/".join(stack)