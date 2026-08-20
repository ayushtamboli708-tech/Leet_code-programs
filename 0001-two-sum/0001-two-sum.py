class Solution(object):
    def twoSum(self, nums, target):
        seen = {} # Stores {value: index}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement is already in our map
            if complement in seen:
                return [seen[complement], i] # Found it! Return indices
            
            # Store current number and its index for future matches
            seen[num] = i
            
        return None # No solution found