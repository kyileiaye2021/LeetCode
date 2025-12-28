class Solution:
    def trap(self, height: List[int]) -> int:
        # prefix = [0,0,1,1,2,2,2,2,3,3,3,3]
        # postfix = [3,3,3,3,3,3,3,2,2,2,1,0]

        prefix = [0] * len(height)
        postfix = [0] * len(height)
        count = 0

        max_prefix = 0
        for i in range(len(height)):
            prefix[i] = max_prefix 
            max_prefix = max(max_prefix, height[i])
        print(prefix)

        max_postfix = 0
        for i in range(len(height) - 1, -1, -1):
            postfix[i] = max_postfix
            max_postfix = max(max_postfix, height[i])
        print(postfix)
        
        for i in range(len(height)):
            min_height = min(prefix[i], postfix[i])
            if min_height - height[i] > 0:
                count += min_height - height[i]

        return count
