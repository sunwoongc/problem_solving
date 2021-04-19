# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return True if len(set(nums)) < len(nums) else False


# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         occurence_dict = {}
#         for i in range(0, len(nums)):
#             occurence_dict.setdefault(nums[i], 0)
#             occurence_dict[nums[i]] += 1
#             if (occurence_dict[nums[i]] == 2):
#                 return True
#         return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        occurence_dict = defaultdict(int)
        for i in range(0, len(nums)):
            occurence_dict[nums[i]] += 1
            if (occurence_dict[nums[i]] == 2):
                return True
        return False
