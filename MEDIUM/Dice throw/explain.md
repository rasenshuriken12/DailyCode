# Dice Throw - Number of Ways Problem

## Problem Statement
Given `m` (number of faces on a die), `n` (number of dice to throw), and `x` (target sum), find the **number of ways to get a sum of x** by rolling `n` dice where each die has `m` faces numbered from 1 to m.

### Example
- **m = 4, n = 2, x = 5**
  - Die 1 shows 1, Die 2 shows 4 → Sum = 5 ✓
  - Die 1 shows 2, Die 2 shows 3 → Sum = 5 ✓
  - Die 1 shows 3, Die 2 shows 2 → Sum = 5 ✓
  - Die 1 shows 4, Die 2 shows 1 → Sum = 5 ✓
  - **Answer: 4 ways**

---

## Approach

### Dynamic Programming (Memoization - Top-Down)
**C++ Solution:**
- Recursively try all outcomes (1 to m) for the current die
- For each face value k, recursively calculate for remaining dice and sum `x-k`
- Base case: `i==0` (no more dice) → check if sum is exactly 0
- Memoize using DP table to avoid recalculation

**State Definition:** `dp[i][s]` = number of ways to get sum `s` using `i` dice

**Recurrence:**
$$dp[i][s] = \sum_{k=1}^{m} dp[i-1][s-k]$$

### Dynamic Programming (Tabulation - Bottom-Up)
**Python Solution:**
- Build from bottom-up: start with 1 die and slowly add more dice
- For each die added, calculate all possible sums it can contribute to
- Use rolling array optimization: maintain only current and next DP states

**Time Complexity:** $O(n \times x \times m)$ - n dice, x possible sums, m faces per die
**Space Complexity:** $O(x)$ - Python uses rolling array; $O(n \times x)$ for C++

---

## Walkthrough (m=4, n=2, x=5)

### C++ Recursive Call Tree:
```
f(2, 5)
├─ f(1, 4) → faces: 1,2,3,4
├─ f(1, 3) → faces: 1,2,3
├─ f(1, 2) → faces: 1,2
└─ f(1, 1) → faces: 1

f(1, 4) = 1 way (face 4)
f(1, 3) = 1 way (face 3)
f(1, 2) = 1 way (face 2)
f(1, 1) = 1 way (face 1)

Total = 1 + 1 + 1 + 1 = 4 ways
```

### Python Iterative Approach:
```
After die 1: dp = [1, 1, 1, 1, 0, ...] (can get 1,2,3,4 each 1 way)
After die 2:
  - From dp[0]=1: can reach 1,2,3,4 (face+0)
  - From dp[1]=1: can reach 2,3,4,5 (face+1)
  - From dp[2]=1: can reach 3,4,5 (face+2)
  - From dp[3]=1: can reach 4,5 (face+3)
  
Result at sum 5: 1+1+1+1 = 4 ways
```

---

## Key Differences Between Solutions

| Aspect | C++ (Memoization) | Python (Tabulation) |
|--------|------------------|-------------------|
| Direction | Top-down (Recursive) | Bottom-up (Iterative) |
| Memory | O(n×x) - 2D DP table | O(x) - Rolling array |
| Clarity | Intuitive recursion | Iterative building |
| Performance | Function call overhead | No recursion overhead |

---

## Edge Cases
1. **x < n** - Impossible (minimum sum is n with all faces showing 1)
2. **x > n*m** - Impossible (maximum sum is n*m with all faces showing m)
3. **n = 0** - Valid only if x = 0
4. **m = 1** - Only 1 way if x = n, else 0 ways

---

## Complexity Analysis
- **Time:** O(n × x × m) - We compute for each of x sums, considering each of n dice, trying m faces
- **Space:** 
  - C++: O(n × x) for memoization table
  - Python: O(x) using rolling array optimization (more efficient!)

