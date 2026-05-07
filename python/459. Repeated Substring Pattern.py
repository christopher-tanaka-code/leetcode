class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        doubled = s + s
        return s in doubled[1:-1]