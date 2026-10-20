class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        tub = 0
        Two additional arrays max_left, max_right
        equation is tub += max(min(max_l, max_R) - h[i], 0)
        '''

        max_left = []
        max_right = [0] * len(height)

        mL = 0
        mR = 0 

        tub = 0

        for i in height:
            max_left.append(mL)
            mL = max(mL, i)

        for i in range(len(max_right) -1, -1, -1):
            max_right[i] = mR
            mR = max(mR, height[i])

        for mL, h, mR in zip(max_left, height, max_right):
            tub += max(0, (min(mL, mR) - h))

        return tub
