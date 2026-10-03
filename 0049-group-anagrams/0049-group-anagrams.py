class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # [0] * 26
        # aa = [2,0,0,...]

        # hashmap {[0,0,0..] : ['eat', 'ate', ...]}
        # iterate thru the strs
        #   create a list of size 26
        #   iterate thru chars
        #       increment the corresponding index
        #       ord(curr char); a : 0, b - 1
        #   if the list not in hashmap
        #       add the list to hashmap with cur str
        #   else 
        #       append the cur str to list
        # res
        # iterate thru the values of the hashmap
        #   add the list values to res list

        group = {}

        for s in strs:
            cur_list = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                cur_list[idx] += 1

            cur_list = tuple(cur_list)

            if cur_list not in group:
                group[cur_list] = [s]
            else:
                group[cur_list].append(s)

            
        res = []
        for g in group.values():
            res.append(g)

        return res

