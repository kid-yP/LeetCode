class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        current_vowel = 0
        max_vowel = 0

        for i in range(k):
            if s[i] in vowels:
                current_vowel += 1
                max_vowel = current_vowel

        for i in range(k, len(s)):
            if s[i] in vowels:
                current_vowel += 1
            if s[i - k] in vowels:
                current_vowel -= 1
            max_vowel = max(max_vowel, current_vowel)

        return max_vowel

        #vowels = set("aeiou")
        #max_vowel_count = 0
    
        #for i in range(len(s) - k + 1):
        #    current_vowel_count = sum(1 for char in s[i:i + k] if char in vowels)
        #    max_vowel_count = max(max_vowel_count, current_vowel_count)
    
        #return max_vowel_count