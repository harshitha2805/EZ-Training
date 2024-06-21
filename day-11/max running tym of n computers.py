class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l=[]
        target=0
        for i in range(len(nums)):
            left = i+1
            right=len(nums)-1
            while left<right:
                if (nums[i]+nums[left]+nums[right])==target and ([nums[i],nums[left],nums[right]]) not in l:
                    l.append([nums[i],nums[left],nums[right]])
                if (nums[i]+nums[left]+nums[right])<target:
                    left+=1
                else:
                    right-=1
        return l