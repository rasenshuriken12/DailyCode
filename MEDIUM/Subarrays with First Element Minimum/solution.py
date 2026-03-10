class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        stack = []
        ans = 0
        
        for i in range(n-1, -1, -1):
            
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if not stack:
                ans += n - i
            else:
                ans += stack[-1] - i
            
            stack.append(i)
        
        return ans

# Example usage:
# sol = Solution()
# print(sol.countSubarrays([3, 4, 1, 6, 2]))  # Output: 11    
