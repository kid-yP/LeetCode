class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = [-p for p in piles]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            reduced = largest - largest // 2
            heapq.heappush(max_heap, -reduced)
        
        return -sum(max_heap)