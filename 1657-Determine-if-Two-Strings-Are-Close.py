class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        def freq(s: str) -> dict:
            count = {}
            for char in s:
                if char in count:
                    count[char] += 1
                else:
                    count[char] = 1
            return count
        
        if len(word1) != len(word2):
            return False

        freq1 = freq(word1)
        freq2 = freq(word2)

        if set(freq1.keys()) != set(freq2.keys()):
            return False
        return sorted(list(freq1.values())) == sorted(list(freq2.values()))