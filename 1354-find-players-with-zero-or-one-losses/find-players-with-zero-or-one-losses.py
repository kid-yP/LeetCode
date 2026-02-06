class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = defaultdict(int)
        players= set()

        for winner, loser in matches:
            losses[loser] += 1
            players.add(winner)
            players.add(loser)
        
        zero_losses = []
        one_losses = []

        for player in players:
            if losses[player] == 0:
                zero_losses.append(player)
            if losses[player] == 1:
                one_losses.append(player)

        return [sorted(zero_losses), sorted(one_losses)]