class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n - 1
        while numbers[right] + numbers[left] != target:
            curr_sum = numbers[right] + numbers[left]
            if curr_sum < target:
                left += 1
            else:
                right -= 1
        
        return [left + 1, right + 1]