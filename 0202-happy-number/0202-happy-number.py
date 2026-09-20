class Solution:
    def isHappy(self, n: int) -> bool:
        num = n 

        visited = set()

        def helper(n):
            total = 0
            while n != 0:
                rem = n % 10
                total += rem ** 2
                n = n // 10

            return total

        while True:
            visited.add(num)
            curr_total = helper(num)
            if curr_total == 1:
                return True

            if curr_total in visited:
                return False
            
            num = curr_total

        return False

