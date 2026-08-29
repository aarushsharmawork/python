class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i in range (len(nums)):
            c = target-nums[i]
            if c in hashtable:
                return (i,hashtable[c])
            hashtable[nums[i]]=i
'''
for this problem i revice dictonary and I also learned some new functions
'''