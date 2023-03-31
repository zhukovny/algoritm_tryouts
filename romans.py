class Solution:
    chars = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M',
    }

    ranges = {
        (1, 4): 1,
        (4, 5): 4,
        (5, 9): 5,
        (9, 10): 9,
        (10, 40): 10,
        (40, 50): 40,
        (50, 90): 50,
        (90, 100): 90,
        (100, 400): 100,
        (400, 500): 400,
        (500, 900): 500,
        (900, 1000): 900,
        (1000, float('inf')): 1000,
    }
    
    def _find_closest(self, num: int) -> int:
        num = abs(num)
        for rng, value in self.ranges.items():
            if num >= rng[0] and num <= rng[1]:
                return value
                    
    
    def intToRoman(self, num: int) -> str:
        if num == 0:
            return ''

        char = self.chars.get(num)
        if char:
            return char
        
        closest = self._find_closest(num)
                
        return self.chars.get(closest) + self.intToRoman(num - closest)
        
print(Solution().intToRoman(3))
