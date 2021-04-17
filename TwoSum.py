# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

#source: Leetcode
#solution: ranjith k
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list1 = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target:
                    list1.append(i)
                    list1.append(j)
        return list1