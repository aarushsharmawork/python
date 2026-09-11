class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1 or num == 0:
            return True
        start, end = 0, num//2
        while start<=end:
            mid = (start+end)//2
            if mid*mid == num:
                return True
            elif mid*mid>num:
                end = mid-1
            else:
                start = mid+1
        return False