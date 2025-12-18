class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)  # count of required characters
        missing = len(t)   # total characters still needed
        left = start = end = 0  # window pointers
        
        # expand the window with right pointer
        for right, char in enumerate(s, 1):
            if need[char] > 0:  # if char is needed
                missing -= 1    # one less missing
            need[char] -= 1     # decrease count in need
            
            # when all chars are found, try to shrink from left
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1  # release extra char
                    left += 1           # move left pointer
                
                # update best window
                if end == 0 or right - left < end - start:
                    start, end = left, right
        
        return s[start:end]  # return minimum window substring
