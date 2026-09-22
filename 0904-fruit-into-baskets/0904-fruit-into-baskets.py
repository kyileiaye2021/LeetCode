class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # findng  k unique ele in the window
        # k = 2

        # hashmap 
        # l, r = 0, 0

        # iterate thru ele wiht r
        #   if r ele not in hashmap
        #       while count size >= k
        #           decrement count[l ele]
        #           if count[l ele] == 0: del count[l ele]
        #           l += 1
        #  
        #    add curr r ele to count or increment count val in count 
        # 
        #    track curr window
        #    update max window
        #    r += 1
        # return max window
        k = 2
        count = {}
        l, r = 0, 0
        max_window = 0

        while r < len(fruits):
            if fruits[r] not in count:
                while len(count) >= k:
                    count[fruits[l]] -= 1
                    if count[fruits[l]] == 0:
                        del count[fruits[l]]
                    l += 1

            count[fruits[r]] = 1 + count.get(fruits[r], 0)
            curr_window = r - l + 1
            max_window = max(max_window, curr_window)
            r += 1

        return max_window



        