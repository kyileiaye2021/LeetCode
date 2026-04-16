class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # "ABAB", k = 2
        # 4

        # "ABABCDAB", k = 2
        # 6

        # "E", k = 0
        # 1

        # "ADBBC", k = 0
        # 3

        # sliding window + two pointer
        # expand from the left
        #   if the duplicate is found
        #       check if k > 0
        #           decrement k
        #           expand more
        #       shrink the window size
        #       remove curr l ele from the set
        #   add the r ele to the set
        #   keep track of the window size
        #   update the longest window size

        l = 0
        r = 0
        longest = 0
        cur_len = 0
        hashmap = {}

        while r < len(s):
            print(s[r])
    
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1

            window_size = r - l + 1
            most_freq = max(hashmap.values())
            while window_size - most_freq > k:
                    hashmap[s[l]] -= 1
                    if hashmap[s[l]] == 0:
                        del hashmap[s[l]]
                    l += 1
                    window_size = r - l + 1
                    most_freq = max(hashmap.values())

            curr_len = r - l + 1
            longest = max(longest, curr_len)
            r += 1

        return longest








        