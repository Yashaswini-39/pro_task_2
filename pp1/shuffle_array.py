class Solution(object):
    def shuffle(self, nums, n):
        result = []
        for index in range(n):
            result.append(nums[index])
            result.append(nums[index + n])
        return result
