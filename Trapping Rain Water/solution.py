class Solution:
    def maxWater(self, arr):
        # code here
        
        n = len(arr)
        
        m1, m2 = 0, 0
        left, right = [0]*n, [0]*n
        for i in range(n):
            m1 = max(m1, arr[i])
            left[i] = m1
            m2 = max(m2, arr[n-i-1])
            right[n-i-1] = m2
        
        water = 0
        for i in range(n):
            water += min(left[i], right[i]) - arr[i]
        return water
        