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

        for base in range(len(nums)-2):
            #Prevents us from processing the same base again
            if nums[base] == nums[base - 1] and base > 0:
                continue

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
                    #don't need bc it's already sorted
                    # combo.sort()

                    #don't need this bc we're skipping everything until we're dealing with new numbers
                    # if combo not in triplets:
                    triplets.append([nums[base], nums[left], nums[right]])

                    right -= 1
                    left += 1

                    '''
                    Right pointer can stick. We want to keep increment left until we hit a new number
                    '''
                    while nums[left - 1] == nums[left] and left < right:
                        left += 1

        return triplets



        