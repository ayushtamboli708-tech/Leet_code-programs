# add two numbers
class Solution(object):
    def twoSum(self, nums, target):
        
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]

            seen[num] = i
lis = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter the target sum: "))
solution = Solution()
result = solution.twoSum(lis, target)
print("Indices of the two numbers that add up to the target:", result)