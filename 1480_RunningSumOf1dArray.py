class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        last = 0
        running_sum = []
        for num in nums:
            running_sum.append(num+last)
            last += num
        return running_sum
