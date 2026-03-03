##(Sliding Window with Counter) Simpler and memory-efficient approach to find the longest subarray with at most k zeros, which effectively gives us the maximum number of 1's we can have by flipping at most k zeros.




class Solution:
    def maxOnes(self, arr, k):
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(arr)):
            if arr[right] == 0:
                zero_count += 1

            while zero_count > k:
                if arr[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len