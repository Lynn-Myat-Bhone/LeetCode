class Solution:
    def twoSum(self, nums: List[int], target: int):

        seen ={} #dictionary
        for idx, value in enumerate(nums):
            diff = target - value 
            if diff in seen:
                return [seen[diff],idx]
            seen[value]= idx
        return None 
            
            
s = Solution()
nums = [2,7,11,15]
target = 9
print(s.twoSum(nums, target))
