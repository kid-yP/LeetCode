class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(math.sqrt(c))

        while i <= j:
            ssum = (i ** 2) + (j ** 2)
            if ssum == c:
                return True
            elif ssum > c:
                j -= 1
            else:
                i += 1
        return False