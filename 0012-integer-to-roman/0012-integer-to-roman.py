class Solution:
    def intToRoman(self, num: int) -> str:
        '''
        Roman integers are from big to small
        So, when converting the integer to roman symbol, divide the num by larger roman num 
        '''
        
        # create a list of list for each symbol and value
        # iterate over the reversed list
        #   check if the number of roman integers that need to be added to res
        #   add the roman integers to the res
        #   update the num by modding the num by the val
        
        
        symbols = [ ['I', 1], ['IV', 4], ['V', 5], ['IX',9], ['X', 10], ['XL', 40],
                   ['L',50], ['XC', 90], ['C',100], ['CD', 400], ['D',500],
                   ['CM', 900], ['M', 1000] ]
        
        res = ''
        for sym, val in reversed(symbols):
            if num // val > 0:
                count = num // val
                res += (sym * count)
                num = num % val
                
        return res

        