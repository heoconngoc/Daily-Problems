class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = len(nums)
        for a in range(0,i):
          for b in range (a+1,i):
            if nums[a] + nums[b] == target:
              return [a, b]
