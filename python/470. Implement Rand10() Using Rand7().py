# The rand7() API is already defined for you.
# def rand7():
#     pass

class Solution:
    def rand10(self) -> int:
        while True:
            # Generate a uniform number from 1 to 49
            num = (rand7() - 1) * 7 + rand7()

            # Use only 1 to 40 because 40 is divisible by 10
            if num <= 40:
                return 1 + (num - 1) % 10