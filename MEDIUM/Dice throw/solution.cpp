/*
========================================
DICE THROW - MEMOIZATION APPROACH (C++)
========================================

Problem: Find number of ways to get sum 'x' by throwing 'n' dice with 'm' faces

Approach: Top-Down Dynamic Programming with Memoization
- State: dp[i][s] = number of ways to get sum 's' using 'i' dice
- Transition: For each face (1 to m), add ways from (i-1 dice, s-face)
- Recurrence: dp[i][s] = sum of dp[i-1][s-k] for k=1 to m

Time Complexity: O(n * x * m) - memoization avoids recomputation
Space Complexity: O(n * x) - 2D DP table

Example: m=4, n=2, x=5
  f(2, 5) tries all faces on die 2:
    + f(1, 4) - die 2 shows 1
    + f(1, 3) - die 2 shows 2
    + f(1, 2) - die 2 shows 3
    + f(1, 1) - die 2 shows 4
  Each f(1, k) returns 1 way, total = 4 ways
========================================
*/

class Solution {
  public:
    int ch;  // ch stores number of faces (m)
    vector<vector<int>> dp;  // 2D DP table for memoization
    
    /**
     * Recursive function to count ways
     * @param i : number of dice remaining to throw
     * @param x : target sum remaining to achieve
     * @return : number of ways to get sum x with i dice
     */
    int f(int i, int x) {
        // BASE CASE 1: No more dice to throw
        // If remaining sum is exactly 0, we found 1 valid way
        // Otherwise, this path is invalid
        if (i == 0) return x == 0;
        
        // BASE CASE 2: Remaining sum is negative
        // Impossible to achieve negative sum, return 0 ways
        if (x < 0) return 0;
        
        // MEMOIZATION: If already computed, return cached result
        if (dp[i][x] != -1) return dp[i][x];
        
        // RECURSIVE CASE: Try all faces on current die
        int total = 0;
        for (int k = 1; k <= ch; k++) {
            // Try rolling 'k' on current die, then solve for (i-1) dice with sum (x-k)
            total += f(i - 1, x - k);
        }
        
        // Store result in DP table and return
        return dp[i][x] = total;
    }
  
    /**
     * Main function to find number of ways
     * @param m : number of faces on each die (1 to m)
     * @param n : number of dice to throw
     * @param x : target sum
     * @return : number of ways to get sum x
     */
    int noOfWays(int m, int n, int x) {
        ch = m;  // Store number of faces
        // Initialize DP table with size (n+1) x (x+1), all values = -1 (not computed)
        dp = vector<vector<int>>(n + 1, vector<int>(x + 1, -1));
        // Start recursion: n dice remaining, sum x needed
        return f(n, x);
    }
};