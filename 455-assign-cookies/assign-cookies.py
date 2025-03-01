class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child_index = 0
        cookie_index = 0

        while child_index < len(g) and cookie_index < len(s):
            if s[cookie_index] >= g[child_index]:
                child_index += 1
            cookie_index += 1
        
        return child_index