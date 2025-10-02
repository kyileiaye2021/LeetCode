class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        if len(start) != len(result):
            return False

        if start.replace('X', '') != result.replace('X',''):
            return False

        l_start = []
        l_end = []
        r_start = []
        r_end = []

        for i in range(len(start)):
            if start[i] == 'L':               
                l_start.append(i)

        for i in range(len(result)):
            if result[i] == 'L':
                l_end.append(i)

        for i in range(len(start)):
            if start[i] == 'R':               
                r_start.append(i)

        for i in range(len(result)):
            if result[i] == 'R':               
                r_end.append(i)

        for i in range(len(l_start)):
            if l_start[i] < l_end[i]:
                return False

        for i in range(len(r_start)):
            if r_start[i] > r_end[i]:
                return False

        return True
    
