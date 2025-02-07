class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        length = len(digits)
        
        # Step 1: Find the pivot
        pivot = -1
        for i in range(length - 2, -1, -1):
            if digits[i] < digits[i + 1]:
                pivot = i
                break
        
        # If no pivot is found, return -1
        if pivot == -1:
            return -1
        
        # Step 2: Find the successor
        for i in range(length - 1, pivot, -1):
            if digits[i] > digits[pivot]:
                # Step 3: Swap the pivot and successor
                digits[i], digits[pivot] = digits[pivot], digits[i]
                break
        
        # Step 4: Reverse the suffix
        digits = digits[:pivot + 1] + digits[pivot + 1:][::-1]
        
        # Convert back to integer
        result = int(''.join(digits))
        
        # Step 5: Check if the result is within the 32-bit signed integer range
        if result > 2**31 - 1:
            return -1
        
        return result