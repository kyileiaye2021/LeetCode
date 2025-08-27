class Solution:
    def dfs(self,rooms, visited, r):
        visited.add(r)

        for key in rooms[r]:
            if key not in visited:
                self.dfs(rooms, visited, key)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        # dfs
        # mark the room as visited
        # go to the neighbors

        # visited 
        # hashmap {room no.: keys}
        # iterate thru the room hashmap
        #   if the room is not visited
        #       call dfs on the room
        # check if the size of visited is the same as num of rooms

        visited = set()
        r = 0 # only the room 0 is unlocked
        self.dfs(rooms, visited, r)

        return len(visited) == len(rooms)
        