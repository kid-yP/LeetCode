class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set('aeiou')
        n = len(word)
        total_count = 0

        for start in range(n):
            vowel_count = {v: 0 for v in vowels}
            consonant_count = 0
            valid_vowel_count = 0
            
            for end in range(start, n):
                char = word[end]
                
                if char in vowels:
                    if vowel_count[char] == 0:
                        valid_vowel_count += 1
                    vowel_count[char] += 1
                else:
                    consonant_count += 1
                
                if valid_vowel_count == 5 and consonant_count == k:
                    total_count += 1
                
                if consonant_count > k:
                    break

        return total_count