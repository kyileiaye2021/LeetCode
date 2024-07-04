class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t) or len(s) > len(t):
            return False
        map = {}
        for char in s:
            if char not in map:
                map[char] = 1
            else:
                map[char] += 1
                
        for letter in t:
            if letter in map and map[letter] > 0:
                map[letter] -= 1
            else:
                return False
        return True