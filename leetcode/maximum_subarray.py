# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         length = len(nums) 
#         sum_array = [nums[0]]
#         for i in range(1, length):
#             sum_array.append(max(nums[i] + sum_array[i-1], nums[i]))
#         return max(sum_array)
# Making extra array storing maximum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        cur_max = 0
        ans = nums[0]
        for i in range(0, length):
            if (cur_max < 0):
                cur_max = 0
            cur_max += nums[i]
            ans = max(cur_max, ans)
        return ans
# Constantly update the maximum, finding out that we don't need to add 'negative value'.
