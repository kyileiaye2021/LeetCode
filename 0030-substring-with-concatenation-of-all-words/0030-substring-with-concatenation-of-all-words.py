class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # happy cases
        # s = "barfoothefoobar", words = ["foo", "bar"]
        # output: [0, 9]

        # s = "barthefoo", words = ["foo", "bar"]
        # output: []

        # edge cases
        # s = "word", words = ["word"]
        # output:[0]

        # s = "word", word = ["yes"]
        # output: []

        # s = "yes", word = ["yes", "no"]
        # output: []

        # s = "foobarthefoobar", word = ["foo", "bar", "the"]
        # output: [0, 3, 6]

        # res list to store the first index of the substring
        # the ele in one window can also be in another window
        # hashmap for the words in words array
        # wordlen = num of words and len of each word
        # slide the str with fixed k = len of each word
        # if the curr word is in the word hashmap
        #   increase the window size
        #   decrement the freq of the ele in the word hashmap
        #   if the window size becomes equal to the wordlen
        #       append the l pointer to the res
        #  iterate left k ele from the window
        #  increment the removed ele freq in word hashmap
        # return res

        res = []
        need = {}

        for w in words:
            need[w] = need.get(w, 0) + 1

        wordLen = len(words[0])
        n = len(words)
        windowLen = n * wordLen

        # iterate thru the eles for num of word len times
        for i in range(wordLen):
            
            left = i
            seen = {}
            count = 0

            for j in range(i, len(s) - wordLen + 1, wordLen):

                curr_word = s[j : j + wordLen]

                # if the word is valid
                if curr_word in need:
                    seen[curr_word] = seen.get(curr_word, 0) + 1
                    count += 1

                    # if the word appears more than 1
                    while seen[curr_word] > need[curr_word]:
                        # shrink the window size
                        left_word = s[left : left + wordLen]
                        seen[left_word] -= 1
                        count -= 1
                        left += wordLen

                    # if count == n
                    if count == n:
                        res.append(left)
                        left_word = s[left : left + wordLen]
                        seen[left_word] -= 1
                        count -= 1
                        left += wordLen

                else:
                    # restart the window
                    # reset the seen hashmap
                    # reset count
                    # move l pointer

                    seen = {}
                    count = 0
                    left = j + wordLen

        return res
                    
                    