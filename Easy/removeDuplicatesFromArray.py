# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class RemoveDuplicatesFromSortedArray:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if i < len(nums) - 2 and nums[i] == nums[i + 1]:
                continue
            nums[count] = nums[i]
            count += 1
        return count