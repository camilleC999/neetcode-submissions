class Solution:
    def maxArea(self, nums: List[int]) -> int:
        '''
        area = (r-l) * min(nums[l], nums[r])
        we start with left and right at 0 and length -1
        we get the area, and compare to a tracking number: max_area = max(max_area, area)
        we want to shift whichever pointer has the shorter height, inwards by one
        when we have equal pointers, then we want to move both pointers inwards by one
            until one of them has a different value
        while l < r
        '''

        max_area = 0
        L, R = 0, len(nums) - 1

        while L < R: 
            area = (R - L) * min(nums[L], nums[R])
            max_area = max(max_area, area)
            if nums[L] < nums[R]:
                L += 1
            elif nums[R] < nums[L]:
                R -= 1
            else:
                R -= 1
                L += 1

        return max_area
