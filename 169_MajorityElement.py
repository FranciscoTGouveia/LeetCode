class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majorityE = nums[0]
        for i in range(len(nums)):
            if count == 0:
                majorityE = nums[i]
            if nums[i] == majorityE:
                count += 1
            else:
                count -= 1
        return majorityE
