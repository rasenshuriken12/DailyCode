# Form the Largest Number

## Problem Statement
Given an array of integers, arrange them in such a way that when concatenated together, they form the largest possible number.

Example: `[3, 9, 30]` → `"9330"` (not `"39330"` or `"30339"`)

## Use Cases
1. **Number Formatting**: Creating maximum values by arranging digit sequences
2. **Database IDs**: Concatenating IDs to form the largest identifier
3. **Data Aggregation**: Combining numeric strings to maximize the result
4. **Competitive Programming**: Optimization problems requiring maximum values
5. **Big Number Assembly**: Creating large numbers from smaller numeric components
6. **Ranking Systems**: Ordering items to produce maximum composite scores

## Solution Approach: Custom Comparator

### Algorithm
1. Convert all integers to strings for easier comparison
2. Define a custom comparator that compares two numbers by concatenating them in both orders
3. If `first + second > second + first`, then `first` should come before `second`
4. Sort the array using this custom comparator
5. Concatenate all sorted strings to form the result
6. Handle edge case: if the result starts with '0', return "0"

### How the Comparator Works

The key insight is: **Instead of comparing numbers directly, we compare their concatenations!**

#### Example: `arr = [3, 9, 30]`

**Step 1:** Compare first = 3 and second = 9
- `first + second = "3" + "9" = "39"`
- `second + first = "9" + "3" = "93"`
- Since `"93" > "39"` (93 is larger), the order is WRONG
- 9 should come before 3, so return **false** (comparator says: swap them!)
- Result: `arr = [9, 3, 30]`

**Step 2:** Compare first = 9 and second = 30
- `first + second = "9" + "30" = "930"`
- `second + first = "30" + "9" = "309"`
- Since `"930" > "309"` (930 is larger), the order is CORRECT
- 9 should come before 30, so return **true** (comparator says: don't swap!)

**Step 3:** Compare first = 3 and second = 30
- `first + second = "3" + "30" = "330"`
- `second + first = "30" + "3" = "303"`
- Since `"330" > "303"` (330 is larger), the order is CORRECT
- 3 should come before 30, so return **true** (comparator says: don't swap!)

**Final Result:** `[9, 3, 30]` → `"9330"` ✓

### Comparator Rule Summary
```
IF order is WRONG (second + first > first + second)  → RETURN FALSE (swap)
IF order is RIGHT (first + second >= second + first) → RETURN TRUE (don't swap)
```

### C++ Implementation
```cpp
static bool compare(int a, int b){
    string s1 = to_string(a);
    string s2 = to_string(b);
    return s1 + s2 > s2 + s1;  // Returns true if order is correct
}

sort(arr.begin(), arr.end(), compare);
```

### Python Implementation
```python
def compare(x, y):
    if x + y > y + x:
        return -1  # x should come before y
    elif x + y < y + x:
        return 1   # y should come before x
    else:
        return 0   # They are equal
        
arr.sort(key=cmp_to_key(compare))
```

## Complexity Analysis

### Time Complexity: O(n log n × k)
- **Sorting:** O(n log n) comparisons
- **Each Comparison:** O(k) where k is the average number of digits
  - String concatenation: O(k)
  - String comparison: O(k)
- **Total:** O(n log n × k)

For practical purposes with reasonable digit counts, this is effectively **O(n log n)**

### Space Complexity: O(n × k)
- **String Array:** O(n) strings
- **Each String:** O(k) characters (where k is average digits per number)
- **Sorting Space:** O(n) for recursion stack (merge sort) or O(1) (quick sort variant)
- **Total:** O(n × k) for input conversion + O(n) for sorting overhead

## Edge Cases

1. **All zeros:** `[0, 0, 0]` → `"0"` (not `"000"`)
2. **Single element:** `[5]` → `"5"`
3. **Already sorted:** `[9, 8, 7]` → `"987"`
4. **Reverse sorted:** `[1, 2, 3]` → `"321"`
5. **Mixed digit counts:** `[3, 30, 34, 5, 9]` → `"9534330"`

## Key Insights

1. **Why not regular sorting?** Regular numerical sorting gives wrong answer: [3, 30, 9] sorts to [3, 9, 30] but "39930" < "39330"

2. **Comparator Logic:** The comparator effectively asks: "Which arrangement produces a larger number?" rather than "Which number is larger?"

3. **Stability:** The custom comparator provides a total ordering that considers the concatenation result

4. **Optimization:** Converting to strings once and reusing is key - avoids repeated string conversions during sorting

## When to Use This Approach

- ✅ When you need to form the **maximum** concatenated number
- ✅ When traditional sorting doesn't work for the problem
- ✅ When you need a custom comparison criterion (not just value comparison)
- ✅ Interview problems involving number arrangement and optimization
