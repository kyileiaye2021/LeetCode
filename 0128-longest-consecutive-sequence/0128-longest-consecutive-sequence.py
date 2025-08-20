class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # iterate thru the list
        #   curr len = 0
        #   check while the neighbor ele is in the list
        #       count the curr len   
        #   update longest 
        # return longest

        longest = 0
        nums = set(nums)

        for ele in nums:

            curr_len = 1
            if ele - 1 not in nums: # this num is a start
                
                ele = ele + 1
                while ele in nums:
                    curr_len += 1
                    ele += 1

            # end = ele
            # while end - 1 in nums:
            #     curr_len += 1
            #     end = end - 1

            longest = max(longest, curr_len)
            print(f"longest: {longest}")

        return longest

