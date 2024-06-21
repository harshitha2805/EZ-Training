#33.Search in a rotated sorted array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        si=0
        li=len(nums)-1
        while(si<=li):
            mid=(si+li)//2
            if (nums[mid]==target):
                return mid
            if (nums[mid]>=nums[si]):
                if (nums[si]<=target and target<=nums[mid]):
                    li=mid-1
                else:
                    si=mid+1
            else:
                if(nums[mid]<=target and target<=nums[li]):
                    si=mid+1
                else:
                    li=mid-1
        return -1