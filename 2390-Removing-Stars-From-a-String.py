class Solution:
    def removeStars(self, s: str) -> str:
        result = []
        for char in s:
            if char != "*":
                result.append(char)
            elif len(result) != 0:
                result.pop()
        return "".join(result)