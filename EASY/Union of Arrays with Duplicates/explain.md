# Union of Arrays with Duplicates

## Problem Statement
Given two arrays `a` and `b` that may contain duplicate elements, find the union of these two arrays. The union should contain all unique elements from both arrays.

**Note:** The arrays may have duplicate elements within themselves, and the union should not contain duplicate values.

## Approach: Hash Set

**Algorithm:**
1. Create an empty set to store unique elements
2. Insert all elements from array `a` into the set
3. Insert all elements from array `b` into the set
4. Convert the set to a result array/list
5. Return the result

**Key Insight:** 
Sets automatically handle duplicates by storing only unique elements. By inserting both arrays into a set, we get all unique elements from both arrays in one data structure.

## Complexity Analysis

### Time Complexity
- **Python Solution:** O(n + m) on average
  - Inserting n elements from array `a`: O(n) average
  - Inserting m elements from array `b`: O(m) average
  - Converting set to list: O(n + m)
  - Total: O(n + m)
  - Worst case (all hash collisions): O((n + m)²) - rare in practice

- **C++ Solution:** O(n + m) on average
  - Creating unordered_set from array `a`: O(n) average
  - Inserting m elements from array `b`: O(m) average
  - Converting to vector: O(n + m)
  - Total: O(n + m)
  - Worst case: O((n + m)²) with poor hash distribution

### Space Complexity
- **Both Solutions:** O(n + m) worst case
  - Set stores all unique elements from both arrays
  - If all elements are unique: O(n + m)
  - If there are duplicates: O(min(n + m, total unique elements))
  - Average: O(number of unique elements)

## Use Cases

### When to use this approach:
- **Finding union of two datasets** - Combining two arrays/lists with automatic deduplication
- **Real-world applications:**
  - Database operations (UNION query)
  - Social network analysis (friend list union)
  - Set operations in mathematics/logic
  - Duplicate removal from combined sources
  - Merging tag lists or categories

### Problem Variations:
- Union of multiple arrays
- Intersection of arrays
- Difference of arrays
- Symmetric difference

## Advantages

1. **Simple & Intuitive:** Easy to understand and implement
2. **Efficient:** O(n + m) time for most cases
3. **Automatic Deduplication:** Sets handle duplicates automatically
4. **Language Built-ins:** Uses standard library data structures
5. **Space-efficient for duplicates:** Saves space when input has many duplicates

## Alternative Approaches

### Approach 1: Using Hash Set (Current)
- Time: O(n + m)
- Space: O(n + m)
- Best for: General case, good performance

### Approach 2: Sorting + Two Pointers
- Time: O((n + m) log(n + m))
- Space: O(1) excluding output
- Best for: When sorted output is required, memory constrained
```cpp
// Sketch: Sort both arrays, use two pointers to merge
```

### Approach 3: Using Map (for counting)
- Time: O(n + m)
- Space: O(n + m)
- Best for: When frequencies are also needed

## Why Hash Set Approach?

**Comparison with alternatives:**

| Approach | Time | Space | Output Order | Best For |
|----------|------|-------|--------------|----------|
| Hash Set | O(n+m) | O(n+m) | Random | General case, optimal |
| Sorting | O((n+m)log(n+m)) | O(1) | Sorted | Small arrays, sorted output |
| Two-pointer (sorted) | O(n+m) | O(1) | Sorted | Pre-sorted arrays |

## Examples

**Example 1: Arrays with duplicates**
```
Input: a = [1, 2, 2, 3], b = [3, 4, 4, 5]
Set from a: {1, 2, 3}
Add b: {1, 2, 3, 4, 5}
Output: [1, 2, 3, 4, 5] (order may vary)
```

**Example 2: Arrays with complete overlap**
```
Input: a = [1, 2, 3], b = [1, 2, 3]
Set: {1, 2, 3}
Output: [1, 2, 3]
```

**Example 3: One empty array**
```
Input: a = [1, 2, 3], b = []
Set: {1, 2, 3}
Output: [1, 2, 3]
```

**Example 4: No common elements**
```
Input: a = [1, 2, 3], b = [4, 5, 6]
Set: {1, 2, 3, 4, 5, 6}
Output: [1, 2, 3, 4, 5, 6] (order may vary)
```

## Implementation Details

### Python Solution Analysis
```python
c = set()              # O(1) - create empty set
for x in a:            # O(n) iterations
    c.add(x)           # O(1) average per add
for x in b:            # O(m) iterations
    c.add(x)           # O(1) average per add
return c               # O(n+m) elements in set
```
- **Simplicity:** Very readable, straightforward logic
- **Efficiency:** Hash-based, optimal performance
- **Note:** Returns a set, not a sorted list

### C++ Solution Analysis
```cpp
unordered_set<int> st(a.begin(), a.end());  // O(n) range constructor
st.insert(b.begin(), b.end());               // O(m) range insert
return vector<int>(st.begin(), st.end());    // O(n+m) conversion
```
- **Efficiency:** Uses range constructors, optimized insertion
- **Flexibility:** Can return vector or other containers
- **Hash Table:** unordered_set for O(1) average operations

## Key Insights

1. **Hash Sets are optimal:** They provide O(1) insertion/lookup on average
2. **Order doesn't matter:** Union doesn't require specific ordering
3. **Automatic deduplication:** No manual duplicate checking needed
4. **Scalability:** Handles large arrays efficiently
5. **Trade-off:** O(n + m) space to achieve O(n + m) time

## Time and Space Comparison

| Operation | Time | Space |
|-----------|------|-------|
| Insert n elements | O(n) avg | O(n) |
| Insert m elements | O(m) avg | O(m) |
| Convert to output | O(n+m) | O(n+m) |
| Total | O(n+m) | O(n+m) |

## Key Takeaway
The hash set approach provides an elegant and efficient solution to find the union of arrays. By leveraging the automatic deduplication property of sets and the O(1) average insertion time, we achieve optimal O(n + m) time complexity without needing to sort or use nested loops.
