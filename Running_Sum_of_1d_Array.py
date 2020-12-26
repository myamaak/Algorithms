import numpy as np
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out=[]
        leng = len(nums)
        for i in range(leng):
            this = nums[:i+1]
            out.append(np.sum(this))
        return out
