class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(segment):
            # Check if the segment is valid
            if len(segment) > 1 and segment[0] == '0':
                return False  # Leading zero
            return 0 <= int(segment) <= 255
        def backtrack(start=0, path=[]):
            # If we have 4 segments and we have used all characters, add to result
            if len(path) == 4 and start == len(s):
                result.append('.'.join(path))
                return
            # If already 4 segments but string not fully used, stop this path
            if len(path) == 4:
                return
            
            # Try segment lengths from 1 to 3
            for length in range(1, 4):
                if start + length <= len(s):
                    segment = s[start:start + length]
                    if is_valid(segment):
                        backtrack(start + length, path + [segment])
        result = []
        backtrack()
        return result