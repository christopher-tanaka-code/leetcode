# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation.
#
# class NestedInteger:
#     def isInteger(self) -> bool:
#         pass
#
#     def getInteger(self) -> int:
#         pass
#
#     def getList(self) -> [NestedInteger]:
#         pass
# """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # Store elements in reverse order so we can pop from the end
        self.stack = nestedList[::-1]

    def next(self) -> int:
        # hasNext guarantees the top is an integer
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]

            if top.isInteger():
                return True

            # Expand the nested list
            self.stack.pop()
            self.stack.extend(top.getList()[::-1])

        return False