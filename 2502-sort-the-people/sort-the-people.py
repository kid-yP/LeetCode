class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        n = len(names)
        for i in range(n):
            max_idx = i
            for j in range(i + 1, n):
                if heights[max_idx] < heights[j]:
                    max_idx = j
                    
            heights[i], heights[max_idx] = heights[max_idx], heights[i]
            names[i], names[max_idx] = names[max_idx], names[i]

        return names


        # n = len(names)
        
        # for i in range(n):
        #     swapped = False
            
        #     for j in range(0, n - i - 1):
        #         if heights[j] < heights[j + 1]:
        #             heights[j], heights[j + 1] = heights[j + 1], heights[j]
        #             names[j], names[j + 1] = names[j + 1], names[j]
                    
        #             swapped = True

        #     if not swapped:
        #         break
        
        # return names
        
        # n = len(names)

        # for i in range(n):
        #     for j in range(0, n - i - 1):
        #         if heights[j] < heights[j + 1]:
        #             heights[j], heights[j + 1] = heights[j + 1], heights[j]
        #             names[j], names[j + 1] = names[j + 1], names[j]

        # return names


        # paired = list(zip(heights, names))
        # paired.sort(reverse=True)
        # return [name for _, name in paired]