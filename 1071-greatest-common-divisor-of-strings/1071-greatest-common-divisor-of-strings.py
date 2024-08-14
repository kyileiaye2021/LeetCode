class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Using the concept of the Greatest Common Divisor (GCD) to find the largest common divisor of the lengths of the two strings.
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        gcd_length = gcd(len(str1), len(str2))
        gcd_str = str1[:gcd_length]
        
        # check if the common divisor str divides both the str1 and str2 
        def is_divisible(s, t):
            if len(s) % len(t) != 0:
                return False
            repeat = len(s) // len(t)
            return (t * repeat == s)
        
        if is_divisible(str1, gcd_str) and is_divisible(str2, gcd_str):
            return gcd_str
        else:
            return ""