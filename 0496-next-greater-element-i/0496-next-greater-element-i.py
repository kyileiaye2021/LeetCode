class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # res = [-1] * len(nums1)
        # iterate thru the nums1
        #   find index in nums2
        #       starting from index iterate thru nums2 
        #           if meet greater ele
        #               add that ele to res[curr i]
        # return res

        # happy cases
        # [4,1,2], [1,3,4,2]
        # [-1,3,-1]

        # hashmap = {num1 val: nums1 index}
        # nxt_ele = [-1] * len(nums2)
        # stack = [] # (val, nums2 idx)

        # iterate thru the nums2
        #       while stack and stack[-1] < nums2 ele :
        #           nums2 ele, nums2 idx = pop the stack 
        #           nums1 idx = find nums2 ele in hashmap
        #           res[nums1 idx] = curr nums2 ele
        #       if nums2 ele in hashmap:
        #           add curr ele to nxt ele

        map = {val: i for i, val in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []

        for i, n in enumerate(nums2):
            while stack and stack[-1][0] < n:
                ele, idx = stack.pop()
                res_idx = map[ele] # idx in nums1
                res[res_idx] = n

            if n in map:
                stack.append((n, i))

        return res


