class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_dict = Counter(s1)
        curr_window = Counter(s2[:len(s1)])
        if s1_dict == curr_window:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            curr_window[s2[l]] -= 1
            curr_window[s2[r]] += 1
            if curr_window == s1_dict:
                return True

            l += 1

        return False 
        