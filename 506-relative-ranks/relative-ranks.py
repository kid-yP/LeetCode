class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(enumerate(score), key=lambda x: x[1], reverse=True)

        ranks = [""] * len(score)
        for i, (index, value) in enumerate(sorted_scores):
            if i == 0:
                ranks[index] = "Gold Medal"
            elif i == 1:
                ranks[index] = "Silver Medal"
            elif i == 2:
                ranks[index] = "Bronze Medal"
            else:
                ranks[index] = str(i + 1)
        
        return ranks