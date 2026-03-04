class Solution:
    def maxSubarrayXOR(self, arr, k):
        n = len(arr)
        
        # Calculate XOR of first window
        current_xor = 0
        for i in range(k):
            current_xor ^= arr[i]
        
        max_xor = current_xor
        
        # Slide the window and update XOR
        for i in range(k, n):
            # Remove the leftmost element of previous window
            current_xor ^= arr[i - k]
            # Add the new rightmost element
            current_xor ^= arr[i]
            max_xor = max(max_xor, current_xor)
        
        return max_xor