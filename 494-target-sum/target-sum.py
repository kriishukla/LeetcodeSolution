class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}
        def count_ways(index, current_sum):

            if (index, current_sum) in dp:
                return dp[(index, current_sum)]

            if index == len(nums):
                return 1 if current_sum == target else 0
\
            ways_with_plus = count_ways(index + 1, current_sum + nums[index])
            ways_with_minus = count_ways(index + 1, current_sum - nums[index])

            total_ways = ways_with_plus + ways_with_minus

            dp[(index, current_sum)] = total_ways

            return total_ways
        return count_ways(0, 0)
