class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        # nums = [12]
        # output: "12"

        # nums = [1, 2]
        # possible - 12 or 21
        # output: "21"

        # nums = [3, 30, 12]
        # possible - 33012 | 31230 | 30312 | 30123 | 12330 | 12303
        # output: "33012"

        # nums = [0]
        # output: "0"

        # Brute force - nested loop - O(n^2)

        # change every ele to str in the list
        # concatenate and compare with cmp_to_key
        # sort the ele aaccording to the compare
        # join the ele 

        # [20,9,34]
        # first compare --> 20, 9
        #   209 < 920
        #   return 1 
        #   [9, 20, 34]
        # second compare --> 20, 34
        #   2034 < 3420
        #   return 1
        #   [9, 34, 20]
        # third compare --> 9 | 34
        #   934 > 349
        #   return -1
        #   [9,34,20]

        # join --> 93420

        for i, n in enumerate(nums):
            nums[i] = str(n)

        print(nums)

        def compare(x, y):
            if x + y > y + x:
                return -1
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(compare))
        print(nums)

        return str(int("".join(nums)))