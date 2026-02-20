class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        h = 0

        for idx, cnt in enumerate(citations):
            if cnt >= idx + 1:
                h = idx + 1
            else:
                break
        
        return h