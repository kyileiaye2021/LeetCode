class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # edge case
        # s = 'a', k = 1
        # output: 1
        
        # s = 'yvp', k = 2
        # output: 0
        
        # create a vowel set - [a, e, i, o, u]
        # max Count = 0
        # curr Count = 0
        
        # itereate thru the first k ele
        #   check if the ele is in the vowel set
        #       increment curr count
        
        # i and i + k, k = 3
        # index - 0
        
        # vowel_set = ['a', 'e', 'i', 'o', 'u']
        # max_count = 0
        # curr_count = 0
        
        # for i in range(len(s) - k + 1):
            
        #     l = i
        #     r = i + k - 1
        #     curr_window_size = r - l + 1
        #     print(f"Left pointer: {l}")
        #     print(f"Right pointer: {r}")
        #     while l <= r:
        #         if s[l] in vowel_set:
        #             curr_count += 1
        #         l += 1
                    
        #     max_count = max(max_count, curr_count)
        #     curr_count = 0
            
        # return max_count 
            

        # # vset = ['a', 'e', 'i', 'o', 'u']
        # # l = 0
        # # r = 0
        # # n =len(s)
        # # count = 0
        # # res = 0
        
        # # while r < k and r < n:
        # #     if s[r] in vset:
        # #         count += 1
        # #     r+=1
        
        # # for i in range(k, n):
        # #     res = max(res, count)
        # #     if s[i] in vset:
        # #         count += 1
        # #     if s[l] in vset:
        # #         count -= 1
        # #     l+=1
        
        # # return res
        
        # iterate thru the list 
        #   count up the vowel if the curr ele is in the list
        #   when the window size becomes k
        #       update the max vowel
        #       move the left pointer
        #       count down the vowel if the curr l points to vowel
        
        vowel_set = ['a', 'e', 'i', 'o','u']
        max_vowel = 0
        curr_vowel = 0
        l = 0
        r = 0
        while r < len(s):
            if s[r] in vowel_set:
                curr_vowel += 1
            
            if (r - l + 1) == k:
                max_vowel = max(max_vowel, curr_vowel)
                if s[l] in vowel_set:
                    curr_vowel -= 1
                l += 1 # shrink the window size
            r += 1
        return max_vowel