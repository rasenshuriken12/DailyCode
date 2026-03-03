# Longest Span in Two Binary Arrays

## Problem Statement
Given two binary arrays `a1` and `a2`, find the longest span `(i, j)` such that:
```
Sum(a1[i...j]) = Sum(a2[i...j])
```

## Core Idea

### Key Insight
The problem is based on the concept that if the sum of elements in a span are equal in both arrays, then:

```
Sum(a1[i...j]) = Sum(a2[i...j])
⟹ Sum(a1[i...j]) - Sum(a2[i...j]) = 0
```

### Algorithm Approach
1. **Difference Array Method**: Instead of comparing sums directly, we construct a difference array:
   ```
   diff[k] = prefixSum(a1, k) - prefixSum(a2, k)
   ```

2. **Problem Reduction**: The original problem reduces to finding the **longest subarray with sum = 0** in the difference array.

3. **Hash Map Technique**: 
   - Store the first occurrence of each prefix sum difference
   - When the same difference appears again, the subarray between these two indices has a sum of 0
   - Track the maximum length span where this occurs

### Dry Run Example
```
a1 = [0, 1, 0, 0, 0, 0]
a2 = [1, 0, 1, 0, 0, 1]

Index   a1  a2  diff(prefix)  Map State
  -1                0:-1         ← Initialize
   0    0   1   -1            -1:0
   1    1   0   0             0:-1 → Match! Length = 1-(-1) = 2
   2    0   1   -1            Seen at 0 → Length = 2-0 = 2
   3    0   0   -1            Seen at 0 → Length = 3-0 = 3
   4    0   0   -1            Seen at 0 → Length = 4-0 = 4 ✓
   5    0   1   -2            -2:5

Answer: 4 (indices 1 to 4)
```

## Complexity Analysis

### Time Complexity: **O(n)**
- Single pass through the array
- HashMap operations (insert, lookup) take **O(1)** on average
- Total: **O(n)** where n is the length of the arrays

### Space Complexity: **O(n)**
- HashMap stores at most **n unique prefix sums**
- In the worst case, all prefix differences are unique
- Total additional space: **O(n)**

## Use Cases

### 1. **Array Balancing Problems**
   - Find spans where two sequences have equal accumulated values
   - Useful in load balancing, resource allocation scenarios

### 2. **Binary Agreement Detection**
   - Determine longest continuous regions where two binary signals match in cumulative value
   - Applications in signal processing, error detection

### 3. **Financial Balance Checking**
   - Finding periods where two accounts have equal transaction sums
   - Debit-Credit balancing in accounting systems

### 4. **Data Consistency Verification**
   - Comparing two data streams for equal cumulative values over time windows
   - Quality assurance in distributed systems

### 5. **Problem Variant Applications**
   - Can be extended to find equal sum subarrays in any two arrays
   - Base for more complex span problems

## Code Implementation Strategy

The solution uses a **Hash Map + Prefix Sum** approach:

1. Maintain a running difference of prefix sums
2. Use a map to track first occurrence of each difference value
3. When a difference repeats, calculate the span length
4. Keep track of the maximum span found

This elegant approach transforms an O(n²) brute force solution into a single-pass O(n) algorithm.