class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        ans = (sorted(nums).index(i) for i in nums)
        return list(ans)
        # a=0
        # ans=[]
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[j]<nums[i]:
        #             a=a+1
        #     ans.append(a)
        #     a=0
        # return ans
a = Solution()
print(a.smallerNumbersThanCurrent(nums = [8,1,2,2,3]))
print(a.smallerNumbersThanCurrent(nums = [6,5,4,8]))
print(a.smallerNumbersThanCurrent(nums = [7,7,7,7]))