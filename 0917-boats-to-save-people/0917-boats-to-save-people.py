class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # happy cases
        # input: people - [1,2], limit = 3
        # output: 1

        # input: people - [1,1], limit = 3
        # output : 1

        # edge cases
        # input: people - [3,2], limit = 3
        # output: 2

        # input: people - [3,2,2,1],limit - 3
        # output: 3

        people.sort()
        boat = 0
        l, r = 0, len(people) - 1

        while l <= r:
            remain = limit - people[r]
            r -= 1
            boat += 1

            # we need to check l <= r again because
            # if people = [1], limit = 2
            if l <= r and people[l] <= remain:
                l += 1
            
        return boat
        