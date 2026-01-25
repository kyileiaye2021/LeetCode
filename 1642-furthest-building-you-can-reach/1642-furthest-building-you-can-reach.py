class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # [4,12,2,7,3,18,20,3
        # happy cases
        # [4,12,2,7,3,18,20,3,19], brick = 10, ladders = 2
        # 7

        # [14,3,19,3]
        # b = 17, ladders =0
        # 3

        # edge cases
        # [1,4,2,6]
        # b = 0, l = 0
        # 0

        # [9]
        # b = 2, l = 1
        # 0

        # [1,4,2,6]
        # b = 0, l = 1
        # 2
        
        # if the bricks --> enough, we use bricks
        # idea - to use ladder for bigger heights but we don't know where those bigger heights are
        # so keep track of the bricks already used
        # if the bricks already used is greater than the bricks that have to use
        #   use the ladder for already used one and use brick for the cur one

        max_heap = []

        for i in range(len(heights) - 1):
            if heights[i] < heights[i + 1]:
                dist = heights[i + 1] - heights[i]

                if dist <= 0:
                    continue

                bricks -= dist
                heapq.heappush(max_heap, -dist)

                # when another gap and there is no brick
                # need to pop out the longer dist to use ladder
                if bricks < 0:
                    if ladders > 0:
                        bigger_height = -heapq.heappop(max_heap)
                        ladders -= 1
                        bricks += bigger_height

                    else:
                        return i

        return len(heights) - 1


