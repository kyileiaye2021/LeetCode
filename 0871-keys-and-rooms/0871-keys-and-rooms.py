class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        # queue and set
        # store the room 0 to queue
        # do it until we find the queue empty
            # pop out and iterate thru every ele in the room 0
            #   if the ele is not in set
            #       add the ele to the queue
        # check if the len of the set is equal to the len of the array

        queue = collections.deque()
        queue.append(0)
        visited = set()

        while queue:
            curr_room = queue.popleft()
            visited.add(curr_room)

            for key in rooms[curr_room]:
                if key not in visited:
                    queue.append(key)

        return len(visited) == len(rooms)


        