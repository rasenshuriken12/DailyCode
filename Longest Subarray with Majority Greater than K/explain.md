# Longest Subarray with Majority Greater than K

## Problem Statement
Given an array `arr` and an integer `k`, find the **longest contiguous subarray** where the **majority of elements are greater than k**.

In other words, the count of elements greater than k should be strictly greater than the count of elements less than or equal to k.

## Core Idea

### Key Insight
Transform the problem using value encoding:
- If `arr[i] > k` → treat as **+1**
- If `arr[i] ≤ k` → treat as **-1**

Now the problem reduces to: **Find the longest subarray with sum > 0**

When sum > 0, it means there are more elements > k than elements ≤ k, which is exactly the "majority" condition.

### Algorithm Approach

1. **Prefix Sum Technique**: Maintain a running sum as we iterate through the array
2. **Direct Match**: If sum > 0 at index i, the subarray [0...i] is valid
3. **HashMap Lookup**: If sum ≤ 0, find if we previously had sum-1
   - If yes, removing that portion leaves us with a subarray of sum > 0
   - Calculate length and update maximum

### Dry Run Example
```
arr = [1, 2, 3, 4]
k = 2

Index   arr[i]  arr[i]>k?  Encoded  Prefix Sum  Action
  -1                                  0          Initialize
   0      1        NO       -1        -1         Look for sum-1=-2 (not found)
   1      2        NO       -1        -2         Look for sum-1=-3 (not found)
   2      3        YES      +1        -1         Look for sum-1=-2 (found at idx 1)
                                                Length = 2-1 = 1
   3      4        YES      +1         0         Look for sum-1=-1 (found at idx 0)
                                                Length = 3-0 = 3 ✓

Answer: 3 (subarray [3, 4])
Majority check: 2 elements > 2, 0 elements ≤ 2 ✓
```

## Complexity Analysis

### Time Complexity: **O(n)**
- Single pass through the array
- HashMap operations (insert, lookup) take **O(1)** on average
- Total: **O(n)** where n is the length of the array

### Space Complexity: **O(n)**
- HashMap stores at most **n unique prefix sums**
- In the worst case, all prefix sum values are distinct
- Total additional space: **O(n)**

## Use Cases

### 1. **Data Quality & Filtering**
   - Quality assurance in manufacturing: Find longest production runs where majority output exceeds quality threshold
   - Network monitoring: Identify longest continuous periods where majority packets exceed size threshold
   - Detect data consistency issues in large datasets

### 2. **Voting & Polling Analysis**
   - Political surveys: Find longest time periods where majority voters favor a candidate (threshold-based)
   - Opinion tracking: Identify sustained periods where majority opinion exceeds satisfaction threshold
   - Jury analysis: Determine longest consistent voting patterns above agreement threshold

### 3. **Financial & Stock Analysis**
   - Trading analysis: Find longest consecutive trading days where majority price points exceed moving average (threshold)
   - Portfolio performance: Identify periods where majority assets outperform benchmark
   - Risk assessment: Track longest duration where majority price changes exceed volatility threshold

### 4. **Sensor Data & IoT**
   - Environmental monitoring: Find longest continuous period where majority temperature readings exceed safe threshold
   - Air quality tracking: Identify longest sustained periods where majority pollution readings exceed limits
   - Machine health: Track longest operation phases where majority sensor values stay above reliability threshold

### 5. **Customer Experience & Satisfaction**
   - Sentiment analysis: Find longest timeframe where majority customer feedback scores exceed satisfaction threshold
   - Employee engagement: Track longest periods where majority satisfaction scores exceed target
   - Service quality: Identify sustained high-performance periods where majority uptime exceeds target

### 6. **Educational Analytics**
   - Student performance: Find longest semester periods where majority test scores exceed passing grade
   - Class performance: Identify sustained high-achievement windows where majority students exceed learning targets
   - Assessment tracking: Longest consecutive assessments where majority scores exceed competency threshold

## Algorithm Intuition

The elegance of this approach lies in **problem transformation**:

1. **Array Encoding**: Instead of complex majority logic, convert to simple +1/-1 encoding
2. **Sum as Metric**: The prefix sum directly represents "excess" (elements > k minus elements ≤ k)
3. **HashMap Trick**: When we can't extend from the beginning, we can "skip" a problematic segment
   - If current sum ≤ 0 and we had sum-1 before, we can remove that segment
   - This is valid because: if removing a segment makes sum > 0, the majority condition is satisfied

## Comparison with Brute Force

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n²) | O(1) | Check all subarrays, calculate sum each time |
| Optimized (HashMap) | **O(n)** | **O(n)** | Single pass with prefix sum caching |

The optimized approach is **essential** for large inputs where n > 10^5.

## Code Implementation Strategy

1. Initialize a hashmap with `sum: 0 → index: -1` (handles subarrays starting from index 0)
2. Iterate through array, maintaining running sum of encoded values
3. If sum > 0: entire prefix is valid, update answer
4. If sum ≤ 0: check if we've seen sum-1 before
   - If yes, length = current_index - previous_index_of_sum_minus_1
   - Update answer with this length
5. Store current sum in hashmap if not already present
6. Return maximum length found
