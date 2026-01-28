from collections import Counter

class Solution:
    def countSubset(self, arr, k):
        n = len(arr)
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        def subset_sums(nums):
            sums = [0]
            for x in nums:
                sums += [s + x for s in sums]
            return sums

        left_sums = subset_sums(left)
        right_sums = subset_sums(right)

        right_count = Counter(right_sums)

        ans = 0
        for s in left_sums:
            ans += right_count[k - s]

        return ans