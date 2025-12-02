from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)

        while i < n:
            # Greedily take as many words as fit.
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])  # one space + next word
                j += 1

            line_words = words[i:j]
            num_words = j - i
            is_last_line = (j == n)

            # Last line OR single-word line => left-justified
            if is_last_line or num_words == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
                res.append(line)
            else:
                # Fully justify
                total_letters = sum(len(w) for w in line_words)
                total_spaces = maxWidth - total_letters
                gaps = num_words - 1

                base = total_spaces // gaps
                extra = total_spaces % gaps  # leftmost gaps get one extra

                parts = []
                for k in range(gaps):
                    parts.append(line_words[k])
                    spaces = base + (1 if k < extra else 0)
                    parts.append(" " * spaces)
                parts.append(line_words[-1])

                res.append("".join(parts))

            i = j

        return res
