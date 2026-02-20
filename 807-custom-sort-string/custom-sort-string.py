class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        res = []

        for ch in order:
            if ch in freq:
                res.append(ch * freq[ch])
                del freq[ch]
        
        for ch, cnt in freq.items():
            res.append(ch * cnt)
        
        return "".join(res)