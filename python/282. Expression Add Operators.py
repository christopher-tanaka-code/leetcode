from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        def dfs(index: int, path: str, value: int, prev: int) -> None:
            if index == len(num):
                if value == target:
                    result.append(path)
                return

            for i in range(index, len(num)):
                # no leading zeros
                if i > index and num[index] == '0':
                    break

                cur_str = num[index:i + 1]
                cur = int(cur_str)

                if index == 0:
                    # first number: no operator before it
                    dfs(i + 1, cur_str, cur, cur)
                else:
                    dfs(i + 1, path + "+" + cur_str, value + cur, cur)
                    dfs(i + 1, path + "-" + cur_str, value - cur, -cur)
                    dfs(i + 1, path + "*" + cur_str, value - prev + prev * cur, prev * cur)

        dfs(0, "", 0, 0)
        return result