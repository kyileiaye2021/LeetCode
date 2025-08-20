class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {(a-z): ['', '']}
        
        anagram = defaultdict(list)
        res = []

        for s in strs:
            curr_code = [0] * 26

            for c in s:
                curr_code[ord(c) - ord('a')] += 1

            curr_code = tuple(curr_code)
            anagram[curr_code].append(s)

        for group in anagram.values():
            res.append(group)

        return res



            
