class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        # Split by '/', empty parts will be ignored naturally
        parts = path.split("/")
        
        for part in parts:
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                # Valid directory name
                stack.append(part)
        
        # Build the canonical path
        return "/" + "/".join(stack)
