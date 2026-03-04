# Max Xor Subarray of size K

## Problem Statement
Given an array and an integer k, find the maximum XOR value of any subarray of size exactly k.

## Approach 1: Sliding Window with Index

### Intuition
Instead of recalculating XOR for each subarray from scratch, we can use a sliding window technique:
- Calculate XOR for the first window of size k
- For the next window, remove the XOR contribution of the leftmost element and add the XOR contribution of the new rightmost element
- Since XOR has the property that `a ^ a = 0`, we can efficiently update: `current_xor = current_xor ^ arr[left] ^ arr[right]`

### Algorithm
1. Initialize `current_xor` with XOR of first k elements
2. Initialize `max_xor` with this value
3. Slide the window from index k to n:
   - Remove the effect of the element going out: `current_xor ^= arr[i - k]`
   - Add the effect of the new element: `current_xor ^= arr[i]`
   - Update `max_xor` if current is larger
4. Return `max_xor`

---

## Approach 2: Two Pointer Logic

### Intuition
Use two pointers (left and right) to maintain a window. The right pointer expands the window, and when the window size exceeds k, the left pointer contracts it. This approach is more explicit about window boundaries and gives visual control over the sliding window.

### Algorithm
1. Initialize `current_xor = arr[0]`, `l = 0`, `r = 1`, `max_xor = INT_MIN`
2. While `l <= n - k`:
   - If window size exceeds k (`r - l + 1 > k`):
     - Update `max_xor` with current window's XOR
     - Remove the leftmost element: `current_xor ^= arr[l]`
     - Move left pointer: `l++`
   - Expand window to the right:
     - Add new element: `current_xor ^= arr[r]`
     - Move right pointer: `r++`
3. Return `max_xor` (or `current_xor` if only one window exists)

### Implementation Details

**Why initialize with `arr[0]`?**
- We start with first element, then gradually build the initial k-sized window by moving `r`

**Window size check `r - l + 1 > k`:**
- The window is too large, so we shrink from the left
- This ensures we only track windows of exactly size k

**Order of operations:**
- Shrink before expand to prevent skipping windows
- Check window size at each iteration while expanding

**Final return logic:**
- If no valid comparison made (`max_xor == INT_MIN`), return the only window found (`current_xor`)
- Otherwise return the maximum XOR found

### Trace Example
```
arr = [8, 10, 3, 6], k = 2

Initial: current_xor = 8, l = 0, r = 1, max_xor = INT_MIN

Iteration 1:
  - r=1: current_xor = 8 ^ 10 = 2, window [8,10]
  - Window size = 2, no shrink
  
Iteration 2:
  - r=2: current_xor = 2 ^ 3 = 1, window [10,3]
  - Window size = 3 > 2, need to shrink
  - max_xor = max(INT_MIN, 1) = 1
  - current_xor = 1 ^ 8 = 9
  - l = 1
  
Iteration 3:
  - r=3: current_xor = 9 ^ 6 = 15, window [3,6]
  - Window size = 3 > 2, need to shrink
  - max_xor = max(1, 15) = 15
  - current_xor = 15 ^ 10 = 5
  - l = 2
  
Loop ends (l = 2 = n - k)
Final answer: 15
```

### Complexity Analysis
- **Time Complexity**: O(n) - single pass through the array
- **Space Complexity**: O(1) - only using few variables

## Comparison

| Aspect | Approach 1 | Approach 2 |
|--------|-----------|-----------|
| Structure | Index-based loop | Two pointers |
| Readability | More direct | More explicit window control |
| Window Init | Pre-calculate first k | Initialize with first element |
| Efficiency | Same O(n) time | Same O(n) time |
| Use Case | Cleaner code | Better window visualization |

## Example
```
arr = [8, 10, 3, 6, 4, 5], k = 2

Windows:
[8, 10] -> XOR = 8 ^ 10 = 2
[10, 3] -> XOR = 10 ^ 3 = 9
[3, 6]  -> XOR = 3 ^ 6 = 5
[6, 4]  -> XOR = 6 ^ 4 = 2
[4, 5]  -> XOR = 4 ^ 5 = 1

Maximum XOR = 9
```

## Key Points
- XOR properties: `a ^ a = 0`, `a ^ 0 = a`, commutative and associative
- Sliding window avoids redundant calculations
- Both approaches are O(n) compared to brute force O(n*k)
