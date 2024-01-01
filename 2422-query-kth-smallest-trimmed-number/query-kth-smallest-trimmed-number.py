from typing import List

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        ans, trimmed = [], {}
        for k, trim in queries:
            trimmed.setdefault(trim, sorted([(num[-trim:], i) for i, num in enumerate(nums)]))
            ans.append(trimmed[trim][k - 1][1])
        return ans
