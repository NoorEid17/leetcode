class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = [asteroids[0]]
        sign = lambda x: 1 if x > 0 else -1
        for asteroid in asteroids[1:]:
            if sign(asteroid) == -1:
                while result and sign(result[-1]) == 1 and abs(result[-1]) < abs(asteroid):
                    result.pop()
                if result == [] or sign(result[-1]) == -1:
                    result.append(asteroid)
                elif abs(result[-1]) > abs(asteroid):
                    pass
                else:
                    result.pop()
            else:
                result.append(asteroid)
        return result
                  