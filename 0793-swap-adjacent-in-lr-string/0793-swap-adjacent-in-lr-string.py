class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        if len(start) != len(result):
            return False

        if start.replace('X', '') != result.replace('X',''):
            return False


        i = 0 # start
        j = 0 # result

        while i < len(start) and j < len(result):

            # if i ele is 'X' --> skip
            while i < len(start) and start[i] == 'X':
                i += 1

            # if j ele is 'X' --> skip
            while j < len(result) and result[j] == 'X':
                j += 1

            # if it becomes the end, both should become. the end
            if i == len(start) and j == len(result):
                return True

            # if one of the arr still has ele to go over
            if i == len(start) or j == len(result):
                return False

            # if they stop before the end, then the curr char pointed by both pointers should be the same
            if start[i] != result[j]:
                return False

            # check if curr char is L
            if start[i] == 'L' and result[j] == 'L':
                if j > i:
                    return False

            # for 'R' 
            if start[i] == 'R' and result[j] == 'R':
                if i > j:
                    return False

            i += 1
            j += 1

        # if start.replace('X', '') != result.replace('X',''):
        #     return False

        # l_start = []
        # l_end = []
        # r_start = []
        # r_end = []

        # for i in range(len(start)):
        #     if start[i] == 'L':               
        #         l_start.append(i)

        # for i in range(len(result)):
        #     if result[i] == 'L':
        #         l_end.append(i)

        # for i in range(len(start)):
        #     if start[i] == 'R':               
        #         r_start.append(i)

        # for i in range(len(result)):
        #     if result[i] == 'R':               
        #         r_end.append(i)

        # for i in range(len(l_start)):
        #     if l_start[i] < l_end[i]:
        #         return False

        # for i in range(len(r_start)):
        #     if r_start[i] > r_end[i]:
        #         return False

        return True
    
