class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist_sq(a, b):
            return (a[0] - b[0])**2 + (a[1] - b[1])**2
        
        points = [p1, p2, p3, p4]
        dists = []
        
        for i in range(4):
            for j in range(i+1, 4):
                dists.append(dist_sq(points[i], points[j]))
        
        dists.sort()

        return (
            dists[0] > 0 and
            dists[0] == dists[1] == dists[2] == dists[3] and
            dists[4] == dists[5] and
            dists[4] == 2 * dists[0]
        )