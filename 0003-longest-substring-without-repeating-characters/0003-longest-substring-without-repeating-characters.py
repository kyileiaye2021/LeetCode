class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # happy cases
        # s = abcabcbb
        # output: 3
        
        # s = 'abccbadeab'
        # output: 4
        
        # edge cases
        # s = 'bbb'
        # outupt: 1
        
        # s = 'abcde'
        # output: 5
        
        # two pointers sliding window
        # when there are duplicates 
       
        # max_len = 0
        # l, r = -1, 0

        # # hold unique characters most recent index
        # visited = {} # {ele: index}
        
        # while r < len(s):
        #     if s[r] in visited and visited[s[r]] > l:
        #         l = visited[s[r]]
        #     visited[s[r]] = r
            
        #     curlen = r - l
        #     if (curlen > max_len):
        #         max_len = curlen
        #     r += 1
        
        # return max_len
        
        # Set solution
        # bcaa
        # #    r
        l = 0
        r = 0
        max_len = 0
        curr_len = 0
        visited = set()
        while r < len(s):
            
            if s[r] in visited:
                while s[r] in visited:
                    visited.remove(s[l])
                    l += 1
                    curr_len -= 1
    
                visited.add(s[r])
                curr_len += 1
                
            else:
                curr_len += 1
                visited.add(s[r])
                max_len = max(curr_len, max_len)
            r += 1
            
        return max_len
        
         
            
        