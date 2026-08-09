from collections import Counter
from typing import List

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Step 1: Count frequency of each character
        count = Counter(s)
        
        # Step 2: Find the first character with count 1
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
                
        # Step 3: If no unique character found
        return -1