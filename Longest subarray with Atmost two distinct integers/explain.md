# Longest Subarray with At Most Two Distinct Integers

## Problem Statement

Given an array of integers, find the **longest subarray that contains at most 2 distinct integers**. Return the length of this subarray.

## Examples

### Example 1:
- **Input:** `arr = [1, 2, 1, 2, 3]`
- **Output:** `4`
- **Explanation:** The longest subarray with at most 2 distinct integers is `[1, 2, 1, 2]` with length 4.

### Example 2:
- **Input:** `arr = [1, 2, 3, 4, 5]`
- **Output:** `2`
- **Explanation:** Any two consecutive elements form the longest subarray with 2 distinct integers. Example: `[1, 2]` or `[4, 5]` with length 2.

### Example 3:
- **Input:** `arr = [1, 1, 1, 1]`
- **Output:** `4`
- **Explanation:** The entire array has only 1 distinct integer, so the answer is 4.

### Example 4:
- **Input:** `arr = [0, 1, 2, 1, 0, 1, 3]`
- **Output:** `5`
- **Explanation:** The longest subarray is `[0, 1, 2, 1, 0]` with at most 2 distinct integers (0 and 1).

## Approach: Sliding Window with Hash Map

### Algorithm Overview

This problem is solved using the **Sliding Window technique** combined with a **Hash Map** to track character/element frequencies:

1. **Initialize**:
   - Two pointers: `i` (left) and `j` (right), both starting at 0
   - Hash map to store distinct element frequencies
   - Variable to track maximum length

2. **Expand window**:
   - Move right pointer `j` forward
   - Add `arr[j]` to the hash map and increment its count

3. **Check constraint**:
   - If number of distinct elements exceeds 2, shrink the window

4. **Shrink window**:
   - Move left pointer `i` forward
   - Decrement count of `arr[i]`
   - Remove element from map if count becomes 0
   - Continue until distinct elements ≤ 2

5. **Track maximum**:
   - After each valid expansion, update maximum length

6. **Return**: The maximum length found

### Why Sliding Window Works

- **Valid window property**: If window at `[i, j]` is valid (≤ 2 distinct), we only need to check if adding `arr[j+1]` violates the constraint
- **Never backtrack**: Once we shrink the window, we never need to expand left pointer again
- **Optimal subarray property**: The longest valid subarray is guaranteed to be found

### Visualization

```
arr = [1, 2, 1, 2, 3]

Step 1: i=0, j=0, add 1
        Window: [1], distinct=1, length=1 ✓

Step 2: i=0, j=1, add 2
        Window: [1,2], distinct=2, length=2 ✓

Step 3: i=0, j=2, add 1
        Window: [1,2,1], distinct=2, length=3 ✓

Step 4: i=0, j=3, add 2
        Window: [1,2,1,2], distinct=2, length=4 ✓

Step 5: i=0, j=4, add 3
        Window: [1,2,1,2,3], distinct=3 ✗ (exceeds 2)
        Shrink: remove arr[0]=1
        Window: [2,1,2,3], distinct=3 (still 3) ✗
        Shrink: remove arr[1]=2
        Window: [1,2,3], distinct=3 (still 3) ✗
        Shrink: remove arr[2]=1
        Window: [2,3], distinct=2, length=2 ✓

Maximum length = 4
```

## Complexity Analysis

### Time Complexity: **O(n)**

- **Why?**: Each element is visited **at most twice**
  - Once when right pointer `j` scans it
  - Once when left pointer `i` removes it
  - Total operations: 2n = O(n)
- Even though there's a while loop, it doesn't increase the overall complexity
- The amortized cost is linear

### Space Complexity: **O(min(n, k))**

- Where `n` is the array length and `k` is the number of distinct elements
- In this problem: **O(1)** or **O(2)** since we store at most 2 distinct elements
- The hash map will never have more than 2 entries
- More generally: Space = O(number of distinct elements allowed) = O(2) = O(1)

## Code Implementation Mapping

### C++ Implementation - Sliding Window with Map

**File**: `solution.cpp`

**Key Features**:
- Uses `map<int, int>` to track frequencies of distinct elements
- Two pointers approach: `i` (left) and `j` (right)
- While loop to shrink window when constraint is violated
- `maxi` variable tracks the maximum window length seen

**Algorithm**:
1. Iterate with right pointer `j` from 0 to n-1
2. Add element to map: `mpp[arr[j]]++`
3. While map size > 2:
   - Decrement left element: `mpp[arr[i]]--`
   - Remove if count becomes 0: `mpp.erase(arr[i])`
   - Move left pointer: `i++`
4. Update max: `maxi = max(maxi, j - i + 1)`
5. Return maxi

**Advantage**: 
- Clean logic with standard STL containers
- Easy to understand and modify
- `map.erase()` automatically handles cleanup

### Python Implementation - Sliding Window with Dictionary

**File**: `solution.py`

**Key Features**:
- Uses `defaultdict(int)` for automatic zero initialization
- Two pointers approach: `i` (left) and `j` (right)
- Dictionary tracking with manual delete operation
- Similar logic to C++ but with Python syntax

**Algorithm**:
1. Initialize `i=0, j=0, maxi=0`
2. While `j < len(arr)` and `i < len(arr)`:
   - Increment count: `dic[arr[j]]+=1`
   - If distinct elements ≤ 2:
     - Update max: `maxi=max(maxi,j-i+1)`
     - Move right: `j+=1`
   - Else (too many distinct):
     - Decrement left: `dic[arr[i]]-=1`
     - Remove if count becomes 0: `del dic[arr[i]]`
     - Move both pointers: `i+=1, j+=1`
3. Final check: `maxi=max(maxi,j-i)`
4. Return maxi

**Advantage**:
- More Pythonic approach
- `defaultdict` eliminates explicit zero-checking
- Concise and readable

## Comparison of Implementations

| Aspect | C++ (Map) | Python (defaultdict) |
|--------|-----------|----------------------|
| **Data Structure** | `map<int, int>` | `defaultdict(int)` |
| **Time Complexity** | O(n log 2) = O(n) | O(n) |
| **Space Complexity** | O(1) | O(1) |
| **Insertion** | O(log 2) amortized | O(1) amortized |
| **Deletion** | O(log 2) with erase() | Manual with del |
| **Size Check** | `.size()` | `len(dict)` |
| **Readability** | Standard STL | Pythonic |
| **Best For** | C++ interviews | Python interviews |

## Use Cases

1. **Substring Problems**: Finding longest substrings with at most k distinct characters (variation)
2. **Data Smoothing**: Group consecutive data points with similar properties
3. **Text Processing**: Analyzing text patterns with limited character sets
4. **Inventory Management**: Finding longest periods using at most 2 product types
5. **Time Series Data**: Finding longest time windows with at most 2 sensor readings
6. **Database Queries**: Detecting sequences matching specific distinctness criteria

## Advantages

- ✅ **Optimal Time**: O(n) linear time complexity
- ✅ **Minimal Space**: O(1) space for storing at most 2 distinct elements
- ✅ **Single Pass**: Process array only once
- ✅ **Scalable**: Can easily extend to "at most k distinct" by changing `<= 2` to `<= k`
- ✅ **No Sorting**: Works on unsorted arrays

## Disadvantages

- ❌ **Space Trade-off**: Uses extra space for hash map (though minimal here)
- ❌ **Not In-Place**: Cannot modify original array structure
- ❌ **Order Sensitive**: Subarray must be contiguous (not subsequence)

## Edge Cases

1. **Empty array**: `[]` → Return 0
2. **Single element**: `[5]` → Return 1 (1 distinct integer)
3. **All same elements**: `[1, 1, 1, 1]` → Return 4 (1 distinct integer)
4. **Two distinct**: `[1, 2, 1, 2, 1]` → Return 5 (entire array)
5. **Strictly increasing**: `[1, 2, 3, 4, 5]` → Return 2 (any two consecutive)
6. **Alternating**: `[1, 2, 1, 2, 1, 2]` → Return 6 (entire array with 2 distinct)

## Extension to "At Most K Distinct"

This solution can be generalized to find the **longest subarray with at most K distinct integers** by simply changing the constraint:

```cpp
while (mpp.size() > k) {  // Change from > 2 to > k
    mpp[arr[i]]--;
    if (mpp[arr[i]] == 0)
        mpp.erase(arr[i]);
    i++;
}
```

This maintains the same O(n) time and O(k) space complexity.

## Key Takeaway

The **Sliding Window** technique is perfect for finding:
- Longest/shortest contiguous subarrays
- Subarrays satisfying constraints (sum, distinctness, frequency)
- Problems where adding/removing elements changes validity in predictable ways

The core insight: Move right pointer to expand, and shrink from left when constraint is violated. Never backtrack the left pointer unnecessarily.
