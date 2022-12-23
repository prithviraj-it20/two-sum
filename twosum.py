Problem link: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            b=target-nums[i]          
            if(b in nums):
                if(nums.index(b)!=i):
                    return[i,nums.index(b)]
