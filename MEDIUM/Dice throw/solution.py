"""
========================================
DICE THROW - TABULATION APPROACH (PYTHON)
========================================

Problem: Find number of ways to get sum 'x' by throwing 'n' dice with 'm' faces

Approach: Bottom-Up Dynamic Programming with Rolling Array Optimization
- State: dp[s] = number of ways to achieve sum 's' using current number of dice
- Transition: For each new die, update all possible sums it can contribute to
- Optimization: Use rolling array to maintain only current and next DP states

Time Complexity: O(n * x * m) - iterate n dice, x sums, m faces
Space Complexity: O(x) - only maintain two arrays of size x

Example: m=4, n=2, x=5
  After die 1: dp[1]=1, dp[2]=1, dp[3]=1, dp[4]=1 (4 ways to get each 1-4)
  After die 2:
    From dp[1]=1: add faces 1,2,3,4 → reach sums 2,3,4,5 each +1 way
    From dp[2]=1: add faces 1,2,3,4 → reach sums 3,4,5,6 each +1 way
    From dp[3]=1: add faces 1,2,3,4 → reach sums 4,5,6,7 each +1 way
    From dp[4]=1: add faces 1,2,3,4 → reach sums 5,6,7,8 each +1 way
  Result: dp[5] = 4 (four ways to get sum 5)
========================================
"""

class Solution:
    def noOfWays(self, m, n, x):
        """
        Count number of ways to get sum x by throwing n dice with m faces
        
        Args:
            m: Number of faces on each die (1 to m)
            n: Number of dice to throw
            x: Target sum
        
        Returns:
            Number of ways to achieve sum x
        """
        # Initialize DP array: dp[s] = number of ways to get sum s
        dp = [0] * (x + 1)
        dp[0] = 1  # Base case: 1 way to get sum 0 (before throwing any dice)
        
        # Process each die one by one
        for die in range(n):
            # Create new DP array for the next die
            new_dp = [0] * (x + 1)
            
            # For each sum achievable with previous dice
            for current_sum in range(x + 1):
                # Only consider sums with non-zero ways
                if dp[current_sum] != 0:
                    # Try all faces on current die
                    for face in range(1, m + 1):
                        # Calculate new sum: previous sum + current face
                        new_sum = current_sum + face
                        
                        # If new sum doesn't exceed target, update it
                        if new_sum <= x:
                            # Add the ways from previous state
                            new_dp[new_sum] += dp[current_sum]
            
            # Update DP for next iteration
            dp = new_dp
        
        # Return number of ways to achieve exactly sum x
        return dp[x]

