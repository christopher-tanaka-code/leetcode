# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation.
#
# class NestedInteger:
#     def __init__(self, value=None):
#         pass
#
#     def isInteger(self):
#         pass
#
#     def add(self, elem):
#         pass
#
#     def setInteger(self, value):
#         pass
#
#     def getInteger(self):
#         pass
#
#     def getList(self):
#         pass
# """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        # If s is just a single integer, return it directly
        if s[0] != "[":
            return NestedInteger(int(s))

        stack = []
        current = None

        num = 0
        sign = 1
        in_number = False

        for ch in s:
            if ch == "[":
                if current is not None:
                    stack.append(current)

                current = NestedInteger()

            elif ch == "-":
                sign = -1

            elif ch.isdigit():
                num = num * 10 + int(ch)
                in_number = True

            elif ch == "," or ch == "]":
                if in_number:
                    current.add(NestedInteger(sign * num))
                    num = 0
                    sign = 1
                    in_number = False

                if ch == "]" and stack:
                    parent = stack.pop()
                    parent.add(current)
                    current = parent

        return current