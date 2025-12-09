class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corner_set = set()
        area_sum = 0
        
        min_x = float('inf')
        min_y = float('inf')
        max_a = float('-inf')
        max_b = float('-inf')
        
        for x, y, a, b in rectangles:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_a = max(max_a, a)
            max_b = max(max_b, b)
            
            area_sum += (a - x) * (b - y)
            
            for corner in [(x, y), (x, b), (a, y), (a, b)]:
                if corner in corner_set:
                    corner_set.remove(corner)
                else:
                    corner_set.add(corner)
        
        expected_corners = {(min_x, min_y), (min_x, max_b), (max_a, min_y), (max_a, max_b)}
        
        return area_sum == (max_a - min_x) * (max_b - min_y) and corner_set == expected_corners