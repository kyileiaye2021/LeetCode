class Solution:
    def rob(self, nums: List[int]) -> int:
        # happy case
        # nums = [1, 2, 3]
        # total = 1 + 3 = 4

        # nums = [1, 2, 3, 4]
        # total = 2 + 4 = 6

        # nums = [2, 1, 1, 2]
        # total = 4

        # nums = [2, 1, 1, 5, 2]
        # total = 6

        # edge case
        # nums = [3]
        # total = 3

        # nums = [1, 4]
        # total = 4

        # Tree (DFS)
        # base case
        # if there is no node, return [0, 0]
        # withRoot = curr val + children's withoutRoot val
        # withoutRoot =  

        # iterative approach
        # if there is only one ele --> we need to return that ele
        # iterate thru the list until the second to last                 ele
        # keep track of the sum of the alternative eles with 2 vars
        # at the end, get the max of the 2 vars and return

        # dynamic programming
        # keep track of the max val with 2 vars - rob1 and rob2
        # if we take rob1 then we can take rob1 + n
        # if we take rob2, we need to skip n
        # we want max --> so we need to do max(rob1 + n , rob2)

        rob1, rob2 = 0, 0
        for n in range(len(nums)):
            temp = max(rob1 + nums[n], rob2)
            rob1 = rob2
            rob2 = temp

        return rob2