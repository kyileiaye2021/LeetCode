class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # edge case
        # input: [0]
        # output: [0]

        # happy case:
        # input: [-2,0]
        # output: [0,4]

        res = [0] * len(nums)
        index = len(nums) -1
        i, j = 0, len(nums) - 1

        while i <= j:
            i_ele = nums[i]**2
            j_ele = nums[j]**2
            if i_ele > j_ele:
                res[index] = i_ele
                i += 1

            else:
                res[index] = j_ele
                j -= 1

            index -= 1

        return res

        
                

                