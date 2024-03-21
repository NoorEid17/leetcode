class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = 0
        max_altitude = 0
        for i in range(1, len(gain) + 1):
            current_altitude = current_altitude + gain[i - 1]
            max_altitude = max(max_altitude, current_altitude)
        return max_altitude