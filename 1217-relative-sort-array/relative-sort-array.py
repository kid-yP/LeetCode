class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {value: index for index, value in enumerate(arr2)}

        def sort_key(x):
            return (order.get(x, len(arr2) + x), x)

        arr1.sort(key=sort_key)

        return arr1