class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # 2 pointers
        # iterate thru the ele for numRows
        # in each iteration
        #   get to the next ele and add it to res str
        #   for getting the next index --> going from 1st row to numRows to back to 1st row 
        #       it take (numRows - 1) * 2 increment steps
        #   for the rows between 0 and last rows, we need to consider to add the num between cols
        #       it depends on row num
        #       row 1 - (increment step - 2)
        #       row 2 - (increment step - 4)
        #       row 3 - (increment step - 6)
        #       row n - (increment step - (n * 2))
        #       we have to add the index to the curr i pos to get to that num

        if numRows == 1:
            return s

        res = ""
        for i in range (numRows):
            # for each i pos
            # we add the i + increment step

            increment = (numRows - 1) * 2 # going down and back to the top
            # jump to the next ele and add it to the res str
            for r in range(i, len(s), increment):
                res += s[r]

                # for the char between cols 
                # they exist between row 0 and last row
                if (i > 0 and i < numRows - 1 and (r + (increment - (i * 2))) < len(s)):
                    res += s[r + (increment - (i * 2))]

        return res