from typing import List


class Solution:
    def method(self, sequence: List[int]) -> int: 
        current = 0
        best = 0
        for n in sequence:
            if n == 1:            
                current += 1
                best = max(best, current)
            else:
                current = 0

        return best
        
        

test_cases = [
    ([1,1,0,1,1,0], 2),
    ([1,1,0,1,1,1], 3),
    ([1,1,1,1,1,], 5),
    ([0,0,0], 0),
    ([], 0),
]
for case, expected in test_cases:
    result = Solution().method(case)
    assert result == expected, f'"{case}": {result} != {expected}'
print('Everything is OK!')
