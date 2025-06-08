class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # incoming -> n-1
        # outgoing --> 0

        # two hashmaps {incoming: num}, {outgoing: num}
        # iterate thru the trust
        #   add the incoming num and outgoing num

        # iterate thru the incoming
        #   return the key that has n -1 incoming and 0 outgoing

        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for src, des in trust:
            incoming[des] += 1
            outgoing[src] += 1
        
        for v in range(1, n + 1):
            if incoming[v] == n - 1 and outgoing[v] == 0:
                return v

        return -1