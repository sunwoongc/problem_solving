class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums) == 0 or k == 0 : return nums
        n = len(nums)
        k %= n
        nums[:] = nums[n-k:] + nums[:n-k]
        return nums
# class Solution:
#   def rotate(self, nums: List[int], k: int) -> None:
#       n = len(nums)
#       k %= n

#       for i in range(0, n-k):
#           nums.append(nums[0])
#           del nums[0]
#       return nums
