#189.Array rotation
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        '''for i in range(k):
            nums.insert(0,nums.pop())'''
        '''for i in range(k):
            temp=nums[len(nums)-1]
            for j in range(len(nums)-1,0,-1):
                nums[j]=nums[j-1]
            nums[0]=temp'''
        if len(nums)==0 or k==0:
            return
        if k>=len(nums):
            k=k%(len(nums))
        a=len(nums)-k
        nums[:]=nums[a:]+nums[:a]