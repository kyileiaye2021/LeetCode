class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # happy cases
        # nums = [0,1,2], k = 1
        # 2

        # nums = [2,1,3], k = 3
        # 2

        # nums = [-1, 0, 1], k = 0
        # 2

        # [-1, 1, - 3, 3], k = 0
        # 3

        # edge cases
        # [0], k = 9
        # 0

        # [], k = 2
        # 0

        # prefix sum + hashmap
        # prefix = [nums[0]]
        # for n in nums from index 1
        #   curr_sum = prefix[-1] + nums[i]
        #   prefix.append(curr_sum)
        #   add curr sum in hashmap with the frequency count

        # total = 0
        # iterate thru the prefix sum 
        #   curr sum - k is in hashmap
        #       add freq count of that diff to total 
        # return total 

        curr_total = 0
        res = 0
        prefix_count = {0: 1}

        for i in range(len(nums)):
            curr_total += nums[i]
            if curr_total - k in prefix_count:
                res += prefix_count[curr_total - k]
            
            prefix_count[curr_total] = 1 + prefix_count.get(curr_total, 0)

        return res
                





        