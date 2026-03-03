# Count Subarrays with Given XOR

## Problem Statement
Given an array of integers and a target value k, find the count of subarrays whose XOR equals k.

A subarray is a contiguous part of the array.

## Approach: Prefix XOR with HashMap

**Algorithm:**
1. Initialize a map/dictionary with {0: 1} (XOR of empty prefix is 0)
2. Maintain a running XOR value that accumulates as we traverse the array
3. For each element:
   - Update running XOR: `running_xor ^= arr[i]`
   - Check if `(running_xor ^ k)` exists in the map
   - If yes, add its count to the answer (subarray from that prefix to current position has XOR = k)
   - Add current `running_xor` to the map
4. Return the total count

**Key Insight:** 
If `prefix[j] ^ prefix[i] = k`, then `prefix[j] = prefix[i] ^ k`
- This property allows us to find previous prefixes that would complete a subarray with XOR = k

## Complexity Analysis

### Time Complexity
- **Python Solution:** O(n)
  - HashMap (defaultdict) operations: O(1) average case
  - Single pass through array: O(n)
  - Total: O(n)

- **C++ Solution:** O(n log n)
  - Map operations (insertion/lookup): O(log n)
  - Single pass through array: O(n)
  - Total: O(n log n)

### Space Complexity
- **Both Solutions:** O(n) worst case
  - Map/dictionary stores up to n unique prefix XOR values
  - In worst case, all prefixes are unique: O(n)
  - Average case: O(min(n, number of unique XOR values))

## Use Cases

### When to use this approach:
- **Subarray problems with XOR:** Any problem asking for count of subarrays with specific XOR property
- **Real-world applications:**
  - Network packet analysis (XOR checksums)
  - Error detection and correction algorithms
  - Bit manipulation problems
  - Problems involving cumulative XOR patterns

### Problem Variations this solves:
- Count subarrays with XOR = k
- Count subarrays with XOR < k (with modifications)
- Find subarray with maximum XOR (with modifications)
- Check if subarray with XOR = k exists

## Advantages

1. **Time Efficient:** O(n) in Python, O(n log n) in C++ - single pass solution
2. **Elegant Logic:** Uses XOR properties (a ^ a = 0, a ^ 0 = a)
3. **Scalable:** Works efficiently for large arrays
4. **Space-Time Tradeoff:** Uses O(n) space to achieve linear/near-linear time

## Why Prefix XOR Approach?

Without this approach, a brute force method would be:
- **Brute Force Time:** O(n²) - checking all subarrays
- **Brute Force Space:** O(1)

The prefix XOR method eliminates nested loops by leveraging XOR properties.

## Examples

**Example 1:**
- Input: arr = [4, 2, 2, 6, 4], k = 6
- Process:
  - i=0: running_xor = 4, check 4^6=2 (not in map), map = {0:1, 4:1}
  - i=1: running_xor = 4^2 = 6, check 6^6=0 (found! ans+=1), map = {0:1, 4:1, 6:1}
  - i=2: running_xor = 6^2 = 4, check 4^6=2 (not in map), map = {0:1, 4:2, 6:1}
  - i=3: running_xor = 4^6 = 2, check 2^6=4 (found! ans+=2), map = {0:1, 4:2, 6:1, 2:1}
  - i=4: running_xor = 2^4 = 6, check 6^6=0 (found! ans+=1), map = {0:1, 4:2, 6:2, 2:1}
- Output: 4 (subarrays: [2,2,6], [2,6,4], [4,2,2,6,4], [6,4])

## Comparison with Other Approaches

| Approach | Time | Space | Best For |
|----------|------|-------|----------|
| Brute Force | O(n²) | O(1) | Small arrays, simplicity |
| Prefix XOR (Python) | O(n) | O(n) | Large datasets, optimal solution |
| Prefix XOR (C++) | O(n log n) | O(n) | Large datasets, when map needed |

## Why Python vs C++ Difference?

- **Python `defaultdict`:** Hash table with O(1) average case operations
- **C++ `map`:** Red-black tree with O(log n) guaranteed operations
- Use `unordered_map` in C++ for O(1) average like Python (though less cache-friendly)

## Implementation Tips

1. Initialize map with `{0: 1}` to handle subarrays starting from index 0
2. Update running XOR before checking the map
3. Check for `running_xor ^ k` (not `running_xor = k`)
4. Add running XOR to map after checking (not before)

## Key Takeaway
The prefix XOR technique transforms a O(n²) brute force problem into a linear time solution by cleverly using a hash table to track previously seen XOR prefixes.
