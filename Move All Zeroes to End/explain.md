# Move All Zeroes to End

## Problem Statement
Given an array containing zeros and non-zero elements, rearrange the array such that all zeroes are moved to the end while maintaining the relative order of non-zero elements. The operation should be done in-place with O(1) extra space.

## Approach: Two-Pointer Technique

### Algorithm Steps

1. **Initialize pointer**: Start with a pointer (e.g., `l` or `last_free`) at index 0, which tracks the position where the next non-zero element should be placed.

2. **Scan the array**: Iterate through the entire array from start to end.

3. **Move non-zero elements**: 
   - When a non-zero element is found, place it at the position pointed to by the pointer.
   - Increment the pointer to the next position.

4. **Fill remaining positions with zeros**: After all non-zero elements are moved to the front, fill all remaining positions from the pointer index to the end with zeros.

5. **Return**: The array is modified in-place with all zeroes at the end.

## Two Implementation Approaches

### Approach 1: Swap-Based (C++)
Uses swapping to move elements:
- When a non-zero element is found at position `i`, swap it with the element at pointer position `l`.
- This is efficient and maintains relative order of non-zero elements.

**Advantage**: Single pass through the array, in-place swaps.

### Approach 2: Direct Placement (Python)
Places non-zero elements directly at the front position:
- First pass: Copy all non-zero elements to the front.
- Second pass: Fill remaining positions with zeros.

**Advantage**: Clear two-phase logic, easier to understand.

### Approach 3: Detailed Two-Pointer with While Loop

This approach uses two pointers with explicit separation of concerns:

1. **Initialize pointers**:
   - `idx`: Index of the array where the next non-zero element should be placed (starts at 0)
   - `i`: Current index being scanned in the array

2. **First phase - For loop (scan and place)**:
   - Iterate through the entire array with pointer `i`
   - Whenever a valid non-zero number is encountered at position `i`:
     - Place it at position `idx`
     - Increment `idx` to the next position
   - This ensures all non-zero elements are compacted at the front

3. **Second phase - While loop (fill zeros)**:
   - After the for loop completes, all non-zero elements have been moved
   - The remaining positions from `idx` to the end MUST contain zeros
   - Use a while loop to explicitly fill all remaining positions with `0`

**Advantage**: Clear separation of logic - collection phase and filling phase are distinct and easy to debug.

**Code Structure**:
```python
idx = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[idx] = arr[i]
        idx += 1

while idx < len(arr):
    arr[idx] = 0
    idx += 1
```

This is essentially what the Python solution implements, making it very readable and maintainable.

### Approach 4: Sequential Zero-NonZero Pairing

This approach takes a different perspective - find zeros and non-zeros sequentially, then pair and swap them:

1. **Find the first zero**: Scan from the start to locate the initial zero position.

2. **Find next non-zero after zero**: Once a zero is found, search ahead for the next non-zero element.

3. **Swap them**: Exchange the zero with the non-zero element found.

4. **Move both pointers**:
   - Move zero pointer to the next zero position
   - Move non-zero pointer to the next non-zero position

5. **Repeat**: Continue until the non-zero pointer reaches the end of the array.

**Advantage**: Intuitive visualization of "pairing" a zero with a non-zero and swapping them.

**Why it works**:
- Systematically finds zeros and immediately replaces them with non-zeros from ahead
- Non-zero elements shift left, zeros accumulate at the end
- Relative order of non-zeros is maintained since we process sequentially from left to right

**Code Concept**:
```python
# Find first zero
i = 0
while i < len(arr) and arr[i] != 0:
    i += 1

# From that position, find and swap with next non-zero
if i < len(arr):
    j = i + 1
    while j < len(arr):
        if arr[j] != 0:
            swap(arr[i], arr[j])
            i += 1
        j += 1
```

## Code Implementation Mapping

### C++ Code - Approach 1: Swap-Based

```cpp
void pushZerosToEnd(vector<int>& arr) {
    int l = 0, sizeOfArr = arr.size();
    for (int i = 0; i < sizeOfArr; i++) {
        if (arr[i]) {
            swap(arr[i], arr[l++]);  // Swap non-zero with position at l
        }
    }
}
```

**Implementation Details**:
- Uses **single-pass approach** with pointer `l` tracking the position for next non-zero element
- **Swap operation**: When `arr[i]` is non-zero, directly swap with `arr[l]` and increment `l`
- **Efficiency**: No second loop needed; zeros naturally fall into place after swaps
- **Working**: 
  - `l` acts as the boundary between non-zero and zero regions
  - Each swap moves a non-zero element to correct position and a zero element backward

### Python Code - Approach 2/3: Direct Placement with Two Phases

```python
def pushZerosToEnd(self, arr):
    last_free = 0
    # Phase 1: Copy all non-zero elements to the front
    for a in arr:
        if a:
            arr[last_free] = a
            last_free += 1
    # Phase 2: Fill remaining positions with zeros
    for i in range(last_free, len(arr)):
        arr[i] = 0
```

**Implementation Details**:
- Uses **two-phase approach** with clear separation of concerns
- **Phase 1 (For loop)**: Iterate through all elements and place non-zero values at positions tracked by `last_free`
- **Phase 2 (For loop)**: Explicitly fill remaining positions from `last_free` to end with zeros
- **Efficiency**: Two linear passes = O(n), maintaining clarity
- **Readability**: Very explicit and easy to understand - first compact non-zeros, then fill zeros

### Comparison Table

| Feature | C++ (Approach 1) | Python (Approach 2/3) | Approach 4 |
|---------|------------------|----------------------|-----------|
| **Method** | Swap both non-zeros and zeros | Direct placement of non-zeros, then fill zeros | Find zero-nonzero pairs and swap |
| **Passes** | 1 pass | 2 passes | 1 pass (with nested search) |
| **Pointer Movement** | Forwards only, both pointers | Forwards in phase 1, phase 2 fills | Finds zero, then searches for next non-zero |
| **Readability** | Compact but tricky | Very explicit and clear | Intuitive visualization |
| **Space** | O(1) | O(1) | O(1) |
| **Time** | O(n) | O(n) | O(n) in best case, O(n²) worst case* |
| **Best For** | Performance-critical | Code clarity, interviews | Understanding the pairing logic |

*Approach 4 worst case: If array has mostly zeros with few non-zeros at the end, inner search can be expensive

## Complexity Analysis

### Time Complexity: **O(n)**
- Where `n` is the size of the array
- **Swap approach**: Single pass through the array - O(n)
- **Direct placement approach**: Two passes through the array - 2×O(n) = O(n)
- No nested loops, making this linear

### Auxiliary Space: **O(1)**
- No additional data structures used
- Only uses a single pointer/counter variable
- Array modification is done in-place
- Not counting the output array space

## Use Cases

1. **Data Cleaning**: Removing zero values from datasets while preserving order of significant values
2. **Matrix Operations**: Processing matrices and moving zero rows/columns to the end
3. **Optimization Problems**: Partitioning elements in algorithms like quicksort or quickselect
4. **Memory Management**: Compacting non-zero elements in sparse arrays
5. **Stream Processing**: Filtering and rearranging data streams in real-time applications
6. **Interview Questions**: Popular algorithmic problem testing two-pointer and in-place modification skills

## Example Walkthrough

**Input**: `[1, 0, 2, 0, 3, 0, 4]`

**Using Swap Approach**:
```
Initial:     [1, 0, 2, 0, 3, 0, 4]  (l=0)
i=0, arr[0]=1 (non-zero):  swap arr[0] and arr[0] → [1, 0, 2, 0, 3, 0, 4]  (l=1)
i=1, arr[1]=0 (zero):      skip
i=2, arr[2]=2 (non-zero):  swap arr[2] and arr[1] → [1, 2, 0, 0, 3, 0, 4]  (l=2)
i=3, arr[3]=0 (zero):      skip
i=4, arr[4]=3 (non-zero):  swap arr[4] and arr[2] → [1, 2, 3, 0, 0, 0, 4]  (l=3)
i=5, arr[5]=0 (zero):      skip
i=6, arr[6]=4 (non-zero):  swap arr[6] and arr[3] → [1, 2, 3, 4, 0, 0, 0]  (l=4)

Final:       [1, 2, 3, 4, 0, 0, 0]
```

## Advantages
- ✅ O(1) auxiliary space (in-place modification)
- ✅ O(n) linear time complexity
- ✅ Maintains relative order of non-zero elements
- ✅ Single pass solution available (swap approach)
- ✅ Works for any data type (integers, floats, objects)

## Disadvantages
- ❌ Requires modification of the original array
- ❌ Swap approach requires careful pointer management
- ❌ Cannot find the count of zeros without iterating again

## Edge Cases

1. **All zeros**: `[0, 0, 0, 0]` → `[0, 0, 0, 0]` (no change)
2. **No zeros**: `[1, 2, 3, 4]` → `[1, 2, 3, 4]` (no change)
3. **Single element**: `[0]` → `[0]` or `[5]` → `[5]`
4. **Alternating zeros**: `[1, 0, 2, 0, 3]` → `[1, 2, 3, 0, 0]`
