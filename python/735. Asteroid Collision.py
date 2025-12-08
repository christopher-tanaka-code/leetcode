class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for asteroid in asteroids:
            # Process collisions only if asteroid is moving left
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    # The top of stack explodes, continue checking
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    # Both explode
                    stack.pop()
                # Current asteroid explodes or both exploded, stop
                break
            else:
                # No collision, push the asteroid onto stack
                stack.append(asteroid)
        
        return stack
