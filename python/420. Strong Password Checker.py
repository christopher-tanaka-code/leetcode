class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        has_lower = any(ch.islower() for ch in password)
        has_upper = any(ch.isupper() for ch in password)
        has_digit = any(ch.isdigit() for ch in password)

        missing_types = 3 - int(has_lower) - int(has_upper) - int(has_digit)

        replacements = 0
        one_delete = 0
        two_delete = 0

        i = 0
        while i < n:
            j = i

            while j < n and password[j] == password[i]:
                j += 1

            length = j - i

            if length >= 3:
                replacements += length // 3

                if length % 3 == 0:
                    one_delete += 1
                elif length % 3 == 1:
                    two_delete += 1

            i = j

        if n < 6:
            return max(missing_types, 6 - n)

        if n <= 20:
            return max(missing_types, replacements)

        deletions_needed = n - 20
        deletions_left = deletions_needed

        # Best deletion case:
        # For groups where length % 3 == 0, one deletion reduces one replacement.
        use = min(deletions_left, one_delete)
        replacements -= use
        deletions_left -= use

        # For groups where length % 3 == 1, two deletions reduce one replacement.
        use = min(deletions_left, two_delete * 2)
        replacements -= use // 2
        deletions_left -= use

        # For all other groups, three deletions reduce one replacement.
        use = deletions_left // 3
        replacements -= use

        replacements = max(0, replacements)

        return deletions_needed + max(missing_types, replacements)