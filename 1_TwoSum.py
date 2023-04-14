"""
The first approach to this problem would be to iterate over the array 
and check all possible pairs of numbers, but that would be 
a O(n²) solution. A less naive approach would be to iterate over
the array and adding the items to an hash table. 
Whenever adding a item, you would check if there is the complement needed
to reach the target in the hash table, giving us a O(n) solution.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {};
        for i in range(len(nums)):
            n = target - nums[i]
            if n not in hash_table:
                hash_table[nums[i]] = i;
            else:
                return [hash_table[n], i]

