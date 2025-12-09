class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # stores indices of temperatures in decreasing order

        for i, temp in enumerate(temperatures):
            # Pop all indices with temperatures less than current temp
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)
        
        return answer
