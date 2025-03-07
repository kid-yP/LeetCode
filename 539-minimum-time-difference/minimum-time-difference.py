class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def toMinutes(time: str) -> int:
            h, m = map(int, time.split(":"))
            return h * 60 + m
        
        minutes = sorted(toMinutes(time) for time in timePoints)
        
        minutes.append(minutes[0] + 1440)
        
        min_diff = float("inf")
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
         
        return min_diff