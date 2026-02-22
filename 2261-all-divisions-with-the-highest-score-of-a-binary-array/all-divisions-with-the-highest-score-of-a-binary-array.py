class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        totalOnes = sum(nums)
        zerosLeft = 0
        onesRight = totalOnes
        scores = []
        maxScore = -1

        for i in range(len(nums)+1):
            score = zerosLeft + onesRight
            scores.append(score)
            maxScore = max(maxScore, score)
            if i < len(nums):
                if nums[i] == 0:
                    zerosLeft += 1
                else:
                    onesRight -= 1

        return [i for i, s in enumerate(scores) if s == maxScore]