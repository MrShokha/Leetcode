class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        s = sum(nums)
        for i in nums:
            while i>0:
                s -= i % 10
                i = i // 10
        return abs(s)
        
a = Solution()
print(a.differenceOfSum(nums = [1,15,6,3]))
print(a.differenceOfSum(nums = [1,2,3,4]))