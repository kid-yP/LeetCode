class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)
        if len_s < len_p:
            return []

        count_s = Counter(s[:len_p])
        count_p = Counter(p)

        result = []

        if count_s == count_p:
            result.append(0)

        for i in range(len_p, len_s):
            count_s[s[i]] += 1
            count_s[s[i - len_p]] -= 1

            if count_s[s[i - len_p]] == 0:
                del count_s[s[i - len_p]]

            if count_s == count_p:
                result.append(i - len_p + 1)

        return result 