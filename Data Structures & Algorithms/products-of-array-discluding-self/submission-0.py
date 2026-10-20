import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fwd = []
        length = len(nums)
        bwd = [0] * length
        result = []

        for idx in range(length):
            if idx == 0:
                fwd.append(nums[idx])
            else:
                fwd.append(fwd[idx -1] * nums[idx])
            
        for idx in range(length - 1, -1, -1):
            if idx == length - 1:
                bwd[idx] = nums[idx]
            else:
                bwd[idx] = bwd[idx + 1] * nums[idx]

        for idx in range(length):
            if idx - 1 < 0:
                result.append(bwd[idx + 1])
            elif idx + 1 == length:
                result.append(fwd[idx - 1])
            else:
                result.append(bwd[idx + 1] * fwd[idx - 1])
        
        return result

        


        return result
                
