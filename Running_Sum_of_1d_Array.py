import numpy as np
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out=[]
        this=0
        leng = len(nums)
        for i in range(leng):
            this += nums[i]
            out.append(np.sum(this))
        return out
