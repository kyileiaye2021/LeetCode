class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        # prefix arr
        # postfix arr
        # subarr_sum = total - prefix at left pos - suffix at right pos
        # return subarr_sum

        prefix_sum = [0] * (len(self.nums) + 1)
        for i in range(len(self.nums)):
            prefix_sum[i + 1] = self.nums[i] + prefix_sum[i]
        
        return prefix_sum[right + 1] - prefix_sum[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)