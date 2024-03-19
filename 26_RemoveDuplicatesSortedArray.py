class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for curr in range(1, len(nums)):
            if nums[index] != nums[curr]:
                index += 1
                nums[index] = nums[curr]
        return index + 1
