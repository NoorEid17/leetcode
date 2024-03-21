class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        dic = {}
        for val in count.values():
            if val in dic:
                return False
            dic[val] = True
        return True