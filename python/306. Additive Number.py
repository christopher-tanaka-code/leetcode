class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            for j in range(i + 1, n):
                first = num[:i]
                second = num[i:j]

                if (len(first) > 1 and first[0] == '0') or (len(second) > 1 and second[0] == '0'):
                    continue

                a = int(first)
                b = int(second)
                k = j

                while k < n:
                    c = a + b
                    c_str = str(c)

                    if not num.startswith(c_str, k):
                        break

                    k += len(c_str)
                    a, b = b, c

                if k == n:
                    return True

        return False