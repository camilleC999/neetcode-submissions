class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        k + j = - anchor
        '''
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []

        nums.sort()
        print("nums: ", nums)
        triplets = []

        base = 0

        while base <= len(nums) - 3:
            left = base + 1
            right = len(nums) - 1
            tgt = - nums[base] 

            while left < right:
                total = nums[left] + nums[right]

                if total > tgt:
                    right -= 1
                elif total < tgt:
                    left += 1
                else:
                    combo = [nums[base], nums[left], nums[right]]
                    combo.sort()
                    if combo not in triplets:
                        triplets.append(combo)

                    right -= 1
                    left += 1

                    while nums[right + 1] == nums[right] and left < right:
                        right -= 1

                    while nums[left - 1] == nums[left] and left < right:
                        left += 1

            base += 1

        return triplets



        