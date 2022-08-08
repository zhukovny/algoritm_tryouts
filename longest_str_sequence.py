
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        char_set = set()
        left = 0
        result = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            result = max(result, len(char_set))

        return result
        
        

test_cases = [
    ("", 0),
    (" ", 1),
    ("a", 1),
    ("bbbbb", 1),
    ("abcabcbb", 3),
    ("pwwkew", 3),
    ("aab", 2),
    ("dvdf", 3),
]
for case, expected in test_cases:
    result = Solution().lengthOfLongestSubstring(case)
    assert result == expected, f'"{case}": {result} != {expected}'
print('Everything is OK!')
