class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        h,c=len(nums),0
        for _ in range (h):
            for l in range (_ +1,h):
             if abs( nums[_] - nums[l])==k:
                c+=1
        return c
