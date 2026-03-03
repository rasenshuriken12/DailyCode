# Missing Element in Range

## Problem Statement
Given an array of integers and a range [low, high], find all elements missing in the range that are not present in the array.

## Use Cases
1. **Data Validation**: Identify missing IDs, sequence numbers, or serial numbers in a dataset
2. **Quality Assurance**: Detect gaps in numerical sequences (e.g., transaction IDs, ticket numbers)
3. **Inventory Management**: Find missing items or stock IDs in a product range
4. **Database Auditing**: Identify missing records or corrupt entries in a range
5. **Number Series Verification**: Check for gaps in continuous number ranges (e.g., employee IDs 101-150)
6. **Price Point Analysis**: Find missing values in a continuous price range for inventory

## Solution Approaches

### Approach 1: HashSet (Easiest)
**Algorithm:**
1. Convert the array into a HashSet for O(1) lookup
2. Iterate through the range [low, high]
3. Check if each number exists in the HashSet
4. Collect all numbers not present in the set

**Time Complexity:** O(n + (high - low + 1))
- O(n) to build the HashSet from the array
- O(high - low + 1) to iterate through the range and check each element

**Space Complexity:** O(n)
- HashSet stores all n elements from the array
- Output array stores at most (high - low + 1) missing elements

**Note:** ⚠️ Simple and straightforward but **requires extra space** for the HashSet!

### Approach 2: HashMap/Unordered Map (C++)
**Algorithm:**
1. Create an unordered_map to store all array elements for O(1) lookup
2. Iterate through the range [low, high]
3. Check if each number exists in the map using O(1) lookup
4. Collect all missing elements

**Time Complexity:** O(n + (high - low + 1))
- O(n) to build the unordered_map from the array
- O(high - low + 1) to iterate through the range and check each element

**Space Complexity:** O(min(n, high - low + 1))
- Unordered_map stores at most n elements from the array
- Output array in worst case stores all elements in the range

### Approach 2: Binary Search (Python)
**Algorithm:**
1. Sort the array
2. For each element in the range [low, high], use binary search (bisect_left) to check existence
3. If the element is not found at the expected position, it's missing

**Time Complexity:** O(n log n + (high - low + 1) × log n)
- O(n log n) for sorting the array
- O(high - low + 1) iterations, each with O(log n) binary search

**Space Complexity:** O(n)
- O(n) for the sorted array
- O(k) for the output array where k is the number of missing elements

### Approach 4: Without HashSet (Messy)
**Algorithm:**
1. Sort the array
2. Skip duplicates using condition `if (arr[i-1] == arr[i]) continue;`
3. Skip values below `low` and break when values exceed `high`
4. Maintain an `expected` pointer that walks through the range [low, high]
5. When there's a gap between `expected` and current array element, fill in all missing numbers
6. Finally, add any remaining numbers from `expected` to `high`

**Time Complexity:** O(n log n + (high - low + 1))
- O(n log n) for sorting the array
- O(high - low + 1) for checking the entire range
- Handles duplicates and boundary conditions explicitly

**Space Complexity:** O(1) excluding output
- **No extra data structures required** (including no HashSet/HashMap)
- Only uses pointer variables and counters
- Output array stores at most (high - low + 1) missing elements

**Note:** ⚠️ This approach works correctly but is verbose and lengthy due to:
- Explicit duplicate handling
- Boundary condition checks
- Multiple pointer management logic
- Less elegant than the clean approach below

### Approach 5: Without HashSet (Clean Code) - RECOMMENDED
**Algorithm:**
1. Sort the array
2. Use a pointer `i` to walk through the sorted array
3. For each number `x` in the range [low, high]:
   - If `arr[i] == x` → element is present, move pointer forward
   - If `arr[i] < x` → advance pointer until `arr[i] >= x`
   - If `arr[i] > x` or we reach the end of array → `x` is missing, add to result
4. Continue until the entire range [low, high] is checked

**Time Complexity:** O(n log n + (high - low + 1))
- O(n log n) for sorting the array
- O(high - low + 1) for iterating through the range [low, high]
- Each array element is visited at most once (pointer moves only forward)

**Space Complexity:** O(1) excluding output
- Only uses a pointer variable and loop variables
- No extra data structures required
- Output array stores at most (high - low + 1) missing elements

## Comparison

| Aspect | HashSet | HashMap | Binary Search | Messy without HS | Clean without HS |
|--------|---------|---------|---------------|-----------------|-----------------|
| **Time Complexity** | O(n + r) | O(n + r) | O(n log n + r log n) | O(n log n + r) | O(n log n + r) |
| **Space** | O(n) | O(min(n, r)) | O(n) | O(1)* | O(1)* |
| **Readability** | Excellent | Good | Moderate | Poor | **Excellent** |
| **Easiest** | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Recommended** | ❌ | ❌ | ❌ | ❌ | ✅ |

*Excluding output array. Where n = array size, r = range size (high - low + 1)

## When to Use Each Approach
- **Use Clean Without HashSet (Approach 5)**: **BEST CHOICE** - Optimal space, clean code, excellent readability, and efficient time
- **Use HashSet (Approach 1)**: When you want the **easiest** and most straightforward solution (if extra space is acceptable)
- **Use HashMap (Approach 2)**: When you want to avoid sorting and the array size is smaller than range size
- **Use Binary Search (Approach 3)**: When the array is pre-sorted or you prefer standard library utilities
- **Use Messy Without HashSet (Approach 4)**: Teaching purpose only - understand why Approach 5 is better
