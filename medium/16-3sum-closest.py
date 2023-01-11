"""
Question 16 3Sum Closest:

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        bestSum = float("inf")

        nums.sort()

        for i in range(0, len(nums) - 2):
            if nums[i] == nums[i-1] and i > 0:
                continue
            lower = i + 1
            upper = len(nums) - 1

            while lower < upper:
                s = nums[i] + nums[lower] + nums[upper]

                if s == target:
                    return s
                if abs(target - s) < abs(target - bestSum):
                    bestSum = s
                
                if s <= target:
                    lower += 1
                    while(nums[lower] == nums[lower -1 ] and lower < upper):
                        lower += 1
                else:
                    upper -= 1
        return bestSum