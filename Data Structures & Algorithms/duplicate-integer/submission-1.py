class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # App-1 (Sorting)

        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False  

        #App-2
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False        