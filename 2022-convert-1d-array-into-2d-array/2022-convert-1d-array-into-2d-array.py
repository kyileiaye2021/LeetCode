class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # happy cases
        # original = [1,2,3,4], m = 2, n = 2
        # output: [[1,2], [3,4]]

        # original = [1,2], m = 1, n = 1
        # output: []

        # create a 2d array of size mxn filled with 0
        # create a pointer to iterate thru the 2d arr
        # create a pointer to iterate thru the original
        # if the pointer becomes out of range, return []
        # add the ele to 2d array
        # return the 2d arr if the org pointer is the size of the original 
        # else return []

        two_d_arr = [[0] * n for _ in range(m)] 
        print(two_d_arr)
        # [[0,0]
        #  [0,0]]
        pt = 0

        for i in range(m):
            for j in range(n):
                print("i" ,i)
                print("j", j)
                print("pt", pt)
                if pt > (len(original) - 1): # if the original pointer out of range
                    return []
                two_d_arr[i][j] = original[pt]
                pt += 1

        return two_d_arr if pt == len(original) else []

        