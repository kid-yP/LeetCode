class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque = deque()
        max_deque = deque()
        left = 0
        max_length = 0

        for right in range(len(nums)):
            while min_deque and nums[right] < nums[min_deque[-1]]:
                min_deque.pop()
            while max_deque and nums[right] > nums[max_deque[-1]]:
                max_deque.pop()

            min_deque.append(right)
            max_deque.append(right)

            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                if min_deque[0] < left:
                    min_deque.popleft()
                if max_deque[0] < left:
                    max_deque.popleft()

            max_length = max(max_length, right - left + 1)

        return max_length