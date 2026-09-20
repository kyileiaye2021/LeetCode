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
            num = helper(num)
            if num == 1:
                return True

            if num in visited:
                return False

        return False

