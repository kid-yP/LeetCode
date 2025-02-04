class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        longest_word = ""

        for word in dictionary:
            if self.is_substring(word, s):
                if(len(word) > len(longest_word)) or (len(word) == len(longest_word) and word < longest_word):
                    longest_word = word
        
        return longest_word

    def is_substring(self, s1 : str, s2: str) -> bool:
        i, j = 0, 0
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i += 1
            j += 1
        return i == len(s1)