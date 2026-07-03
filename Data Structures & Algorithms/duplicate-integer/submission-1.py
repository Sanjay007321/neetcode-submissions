class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)-1,-1,-1):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False
