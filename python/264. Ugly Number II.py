class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglies = [1] * n
        i2 = i3 = i5 = 0

        for i in range(1, n):
            next2 = uglies[i2] * 2
            next3 = uglies[i3] * 3
            next5 = uglies[i5] * 5

            next_ugly = min(next2, next3, next5)
            uglies[i] = next_ugly

            if next_ugly == next2:
                i2 += 1
            if next_ugly == next3:
                i3 += 1
            if next_ugly == next5:
                i5 += 1

        return uglies[-1]