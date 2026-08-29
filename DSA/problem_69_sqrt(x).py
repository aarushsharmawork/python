'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        if x == 0:
            return 0
        start = 0
        end = x
        ans = 0
        while (start<=end):
            mid = start + (end-start)//2
            if mid*mid>x:
                end = mid-1
            elif mid*mid == x:
                return mid
            else:
                start = mid + 1
                ans = mid       
        return ans

'''
# This first code was the first initial code that i wrote but it was taking too much memory.
# So than I wrote the 2nd code for the purpose of optimisation and less memory consumption.
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        if x == 0:
            return 0
        start = 0
        end = x//2
        ans = 0
        while (start<=end):
            mid = start + (end-start)//2
            if mid*mid>x:
                end = mid-1
            elif mid*mid == x:
                return mid
            else:
                start = mid + 1
                ans = mid       
        return ans

# I also learned binary search with this problem