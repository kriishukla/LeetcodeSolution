class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def count_combinations(amount, index):
            if (amount, index) in dp:
                return dp[(amount, index)]

            if amount == 0:
                return 1

            if index == len(coins) or amount < 0:
                return 0

            include_current = count_combinations(amount - coins[index], index)

            exclude_current = count_combinations(amount, index + 1)

            total_combinations = include_current + exclude_current

            dp[(amount, index)] = total_combinations

            return total_combinations
        return count_combinations(amount, 0)
