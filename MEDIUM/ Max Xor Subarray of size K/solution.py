class Solution:
    def maxSubarrayXOR(self, arr, k):
        from functools import reduce
        lth=len(arr)
        mx=cur=reduce(lambda x,y:x^y,arr[:k])
        for right in range(k,lth):
            cur^=arr[right]^arr[right-k]
            mx=max(mx,cur)
        return mx