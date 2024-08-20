# Problem: Asteroid Collision - https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        for asteroid in asteroids:
            if not stack or asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and abs(asteroid) > stack[-1] and stack[-1] > 0:
                    stack.pop()
                
                if stack and abs(asteroid) == stack[-1]:
                    stack.pop()
                else:
                    if not stack or stack[-1] < 0:
                        stack.append(asteroid)
        return stack
                    
       