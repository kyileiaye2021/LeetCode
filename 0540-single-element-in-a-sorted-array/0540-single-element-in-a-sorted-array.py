class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # happy cases
        # nums = [1,1,2,3,3,4,4,8,8]
        # 2
        # nums = [3,3,7,7,10,11,11]
        # 10

        # edge cases
        # nums = [6,7,7]
        # 6

        # nums = [7]
        # otuput: 7

        # mid 
        # if mid - 1 >=0 and mid + 1 < len(nums) and mid ele is not equal to mid - 1 ele and mid + 1 ele 
        #   return mid ele
        # if mid - 1 ele == mid ele
        #    i =  mid - 1
        #    j = mid
        # if mid + 1 ele == mid ele 
        #   i = mid
        #   j = mid + 1
        # if len(nums[:i]) % 2 ==0:
        #   l = j + 1
        # else:
        #   r = i - 1

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if (mid - 1 < 0 or nums[mid - 1] != nums[mid]) and (mid + 1 >= len(nums) or nums[mid + 1] != nums[mid]):
                return nums[mid]

            left_size = mid - 1 if nums[mid - 1] == nums[mid] else mid

            if left_size % 2 == 0:
                l = mid + 1

            else:
                r = mid - 1