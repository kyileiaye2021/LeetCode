class Solution:
    def reorganizeString(self, s: str) -> str:

        # s = "a"
        # output: a

        # s = "aabb"
        # output: abab

        # s = "aaaa"
        # output: ""
        
        # s= "abcd"
        # output: "abcd"

        # s = "aabc"
        # output: "abac"

        # s = "aabcc"
        # output: "abcac"

        # max heap (count, char)
        # queue - for remaining char (index, count, char)
        s_freq = Counter(s)
        max_heap = [(-f, c) for c, f in s_freq.items()]
        heapq.heapify(max_heap)

        queue = deque()
        res = ""

        index = 0
        while max_heap:
            f, c = heapq.heappop(max_heap)
            res += c
            index += 1
            rem = -f - 1
            if rem > 0: # add the ele to cool down (same not to be adjacent)
                queue.append((index +1, rem, c))

            if queue and index == queue[0][0]: # adding the rem char back to max heap if it allows
                index, f, c = queue.popleft()
                heapq.heappush(max_heap, (-f, c))

        print(res)
        return res if not queue else ""

            



