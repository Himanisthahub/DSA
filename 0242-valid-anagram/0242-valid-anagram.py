from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            counter_s = Counter(s)
            counter_t = Counter(t)
            return counter_s == counter_t
