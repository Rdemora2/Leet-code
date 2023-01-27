# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index1 = 0
        while True:
            for index2 in range(index1+1,len(nums)):
                if nums[index1] == target - nums[index2]:
                    return [index1,index2]       
            index1+=1