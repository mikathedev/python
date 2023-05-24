class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mat = max(set(nums), key = nums.count)
        counter = 0
        numsl = len(nums)
        while mat in nums:
            nums.remove(mat)
            counter = counter + 1

        deChance = counter / numsl
        if deChance > 2/3:
            return(True)
        else:
            return(False)

