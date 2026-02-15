class Solution:
    def isValid(self, s: str) -> bool:
        stack = ""
        pairs = {")": "(", "]": "[", "}": "{"}

        for ch in s:
            if ch in pairs.values():
                stack += ch
            else:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack = stack[:-1]

        return not stack
