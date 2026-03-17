class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0  # pointer for s
        j = 0  # pointer for p
        star = -1  # most recent position of '*'
        match = 0  # position in s when last '*' was found

        while i < len(s):
            # Case 1: current characters match, or pattern has '?'
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1

            # Case 2: pattern has '*', record its position
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1

            # Case 3: mismatch, but we saw a previous '*'
            # Let that '*' absorb one more character from s
            elif star != -1:
                j = star + 1
                match += 1
                i = match

            # Case 4: mismatch and no '*' to recover with
            else:
                return False

        # Remaining characters in p must all be '*'
        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)