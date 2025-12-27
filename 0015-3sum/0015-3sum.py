class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # nums = [0,1,1]
        # output: []

        # nums = [0,0,0]
        # output: [0,0,0]

        # nums = [1,-1,0]
        # output: [1, -1, 0]

        # nums = [1, -1, 0, -1]
        # output: [1, -1, 0]

        # nums = [1, -1, 0, -1, 1, 0]
        # output: [[1, -1, 0], [-1, 1, 0]]

        # nums =[-1, 0, 1, 2, -1, -4]
        # output: [[-1,-1,2], [-1, 0, 1]]

        # [-4, -1, -1, -1,  0, 2, 2]

        res = []
        # sort the arr
        nums = sorted(nums)

        # iterate thru the arr
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            curr = nums[i]
        

            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] + curr < 0:
                    l += 1

                elif nums[l] + nums[r] + curr > 0:
                    r -= 1

                else:
                    res.append([curr, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1

        return res
        # l and r pointer for the other ele in the arr to the right of curr

        # apply binary search on the remaining arr
