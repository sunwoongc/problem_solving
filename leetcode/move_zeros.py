class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        length = len(nums)
        zero = []
        nonzero = []
        for i in range(0, length):
            if (nums[i] == 0):
                zero.append(0) 

            else:
                nonzero.append(nums[i]) 
                
        for i in range(0, len(nonzero)):
            nums[i] = nonzero[i]
        for i in range(0, len(zero)):
            nums[len(nonzero) + i] = zero[i]

        return nums
      
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         length = len(nums)
#         nonzeroPointer = 0
#         for i in range(0, length):
#             if (nums[i] != 0):
#                 nums[nonzeroPointer] = nums[i]
#                 nonzeroPointer += 1
#         for i in range(nonzeroPointer, length):
#             nums[i] = 0

#         return nums
        
                
        
