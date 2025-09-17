class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        for i, n in enumerate(nums):
            nums[i] = str(n)

        nums.sort(key=lambda x: x * 10, reverse=True)

        print(nums)
        return str(int(''.join(nums)))
