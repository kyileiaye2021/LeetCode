class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #create a variable to keep track of index which is not equal to val
        #iterate over the nums
        #check the curr item == val
        #if not, update the var

        k = 0
        for item in nums:
            if item != val:
                nums[k] = item
                k += 1
        return k