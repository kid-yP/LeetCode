class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(math.sqrt(c))

        while a <= b:
            curr_sum = a * a + b * b
            if curr_sum == c:
                return True
            elif curr_sum < c:
                a += 1
            else:
                b -= 1

        return False