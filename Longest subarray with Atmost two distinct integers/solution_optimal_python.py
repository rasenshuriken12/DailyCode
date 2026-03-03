from collections import defaultdict

class Solution:
    # ============================================================================
    # OPTIMAL PYTHON SOLUTION: Sliding Window Magic - At Most Two Distinct Integers
    # ============================================================================
    # Time Complexity: O(n) - Each element processed at most twice (by high and low)
    # Space Complexity: O(1) - Map stores at most 3 distinct elements (constant)
    #
    # ============================================================================
    # 🔍 INTUITION
    # ============================================================================
    # The problem requires finding the longest subarray with AT MOST 2 distinct
    # integers. This is a classic sliding window problem where we:
    # 1. Maintain a "window" (contiguous subarray) that satisfies the constraint
    # 2. Dynamically expand and shrink the window
    # 3. Track the maximum valid window size
    #
    # Key Insight: When we know one boundary is "fixed", the other forms a
    # bottleneck. We process from the constraint boundary and expand from
    # the free boundary.
    #
    # ============================================================================
    # 🚀 APPROACH: SLIDING WINDOW TECHNIQUE
    # ============================================================================
    # Use two pointers:
    # - low (left pointer): Left boundary of current window
    # - high (right pointer): Right boundary of current window
    #
    # Hash Map for Tracking:
    # - A map stores the frequency of elements in the current window
    # - If an element's count drops to 0, remove it from the map
    # - len(map) tells us the number of DISTINCT elements
    #
    # Window Validity:
    # - Valid window: len(map) ≤ 2 (at most 2 distinct integers)
    # - Invalid window: len(map) > 2 (too many distinct integers)
    #
    # ============================================================================
    
    def totalElements(self, arr):
        # ========================================================================
        # INITIALIZATION
        # ========================================================================
        # low: Left pointer of the sliding window (starts at index 0)
        # high: Right pointer of the sliding window (starts at index 0)
        # mp: Frequency map of elements in current window
        #     Key = element value, Value = frequency
        # ans: Maximum length found so far
        
        low = 0                             # Left boundary of window
        high = 0                            # Right boundary of window
        mp = defaultdict(int)               # Frequency map {element: count}
        ans = 0                             # Maximum window length
        
        # ========================================================================
        # EXPAND THE WINDOW: Move high pointer
        # ========================================================================
        # Process each element by moving the high pointer from left to right
        
        while high < len(arr):
            # Step 1: Add current element to the window
            # This expands the window to include arr[high]
            mp[arr[high]] += 1
            
            # ====================================================================
            # SHRINK THE WINDOW: Move low pointer if needed
            # ====================================================================
            # If we have MORE than 2 distinct elements, shrink from left
            # Continue shrinking until we have ≤ 2 distinct elements
            
            while len(mp) > 2:
                # Decrement frequency of the leftmost element
                mp[arr[low]] -= 1
                
                # If frequency becomes 0, the element is out of the window
                # Remove it from map to keep distinct count accurate
                if mp[arr[low]] == 0:
                    del mp[arr[low]]
                
                # Move left pointer forward (shrink window from left)
                low += 1
            
            # ====================================================================
            # TRACK MAXIMUM: Update answer when window is valid
            # ====================================================================
            # After shrinking, window [low, high] is valid (≤ 2 distinct)
            # Calculate current window length and update maximum
            current_length = high - low + 1
            ans = max(ans, current_length)
            
            # ====================================================================
            # EXPAND FURTHER: Move high pointer for next iteration
            # ====================================================================
            # Continue expanding to explore more windows
            high += 1
        
        return ans


# ============================================================================
# 📝 DETAILED WALKTHROUGH EXAMPLE
# ============================================================================
"""
Array: [1, 2, 1, 2, 3]

Initial: low=0, high=0, mp={}, ans=0

HIGH=0: Add arr[0]=1
        mp={1:1}, len(mp)=1 ≤ 2 ✓ Valid
        current_length = 0-0+1 = 1, ans = 1
        Window: [1]
        
HIGH=1: Add arr[1]=2
        mp={1:1, 2:1}, len(mp)=2 ≤ 2 ✓ Valid
        current_length = 1-0+1 = 2, ans = 2
        Window: [1, 2]
        
HIGH=2: Add arr[2]=1
        mp={1:2, 2:1}, len(mp)=2 ≤ 2 ✓ Valid
        current_length = 2-0+1 = 3, ans = 3
        Window: [1, 2, 1]
        
HIGH=3: Add arr[3]=2
        mp={1:2, 2:2}, len(mp)=2 ≤ 2 ✓ Valid
        current_length = 3-0+1 = 4, ans = 4
        Window: [1, 2, 1, 2]
        
HIGH=4: Add arr[4]=3
        mp={1:2, 2:2, 3:1}, len(mp)=3 > 2 ✗ Invalid!
        
        SHRINK FROM LEFT (len(mp) > 2):
        
        low=0: Remove arr[0]=1
               mp[1]-- → mp={1:1, 2:2, 3:1}
               len(mp)=3 still > 2, continue
               low++ → low=1
        
        low=1: Remove arr[1]=2
               mp[2]-- → mp={1:1, 2:1, 3:1}
               len(mp)=3 still > 2, continue
               low++ → low=2
        
        low=2: Remove arr[2]=1
               mp[1]-- → mp={1:0, 2:1, 3:1}
               mp[1]==0, so delete → mp={2:1, 3:1}
               len(mp)=2 ≤ 2 ✓ Valid
               low++ → low=3
        
        current_length = 4-3+1 = 2, ans = max(4, 2) = 4
        Window: [2, 3]
        
HIGH=5: Loop ends (high >= len(arr))

FINAL ANSWER: ans = 4
The longest valid subarray is [1, 2, 1, 2] with length 4
"""

# ============================================================================
# ⏳ TIME & SPACE COMPLEXITY ANALYSIS
# ============================================================================
"""
TIME COMPLEXITY: O(n)
- The key insight: each element is processed AT MOST TWICE
  1. Once when high pointer includes it (expansion)
  2. Once when low pointer excludes it (shrinkage)
- Even though we have nested while loop, the total operations across all
  iterations is 2n = O(n)
- This is because:
  - high pointer goes from 0 to n-1 once (n steps)
  - low pointer goes from 0 to n-1 once (n steps)
  - Total combined: 2n steps
- The while loop doesn't restart from beginning; it continues from where it left

SPACE COMPLEXITY: O(1) or O(k) where k = 2
- The map (dictionary) stores ONLY the distinct elements present in the window
- Due to our constraint, the map will NEVER have more than 3 entries
  (because we shrink as soon as we have 3 distinct elements)
- Since k=2 is constant in this problem, space is O(1)
- More generally, for "at most k distinct": space would be O(min(k, n))
  but since k=2 here, it's effectively O(1)

SPACE BREAKDOWN:
- mp (defaultdict): O(1) - at most 2-3 entries
- low, high, ans (integers): O(1) - constant space
- Total: O(1)
"""

# ============================================================================
# 🎯 KEY INSIGHTS & TRICKS
# ============================================================================
"""
1. VALIDITY TRACKING:
   - We check len(mp) to know count of distinct elements
   - If len(mp) ≤ 2, window is valid
   - If len(mp) > 2, window is invalid (too many distinct)

2. SHRINKING STRATEGY:
   - Always shrink from the LEFT (low pointer)
   - This preserves the longest possible window
   - We shrink only as much as needed (until len(mp) ≤ 2)

3. UPDATE TIMING:
   - We update ans AFTER shrinking (after window is valid)
   - This ensures we only count valid windows

4. ELEMENT REMOVAL:
   - When mp[arr[low]]==0, we must DELETE the key
   - If we don't delete, len(mp) won't decrease correctly
   - Deletion is crucial for accurate distinct count

5. POINTER MOVEMENT:
   - high pointer: Always moves forward (expands window)
   - low pointer: Moves forward when needed (shrinks window)
   - Both move only right; never backtrack

6. MONOTONICITY:
   - As high increases, the window gets larger or stays same
   - We never "restart" or "backtrack"
   - This ensures linear time complexity

7. GENERALIZABLE:
   - To find "at most K distinct", just change "len(mp) > 2" to "len(mp) > k"
   - Time and space complexity remain same: O(n) and O(k)
   - This makes the solution scalable
"""

# ============================================================================
# 📋 ALGORITHM STEPS SUMMARY
# ============================================================================
"""
STEP 1: INITIALIZATION
   - Set low = 0, high = 0, mp = {}, ans = 0

STEP 2: EXPAND WINDOW
   - Add arr[high] to mp
   - Increment mp[arr[high]]

STEP 3: CHECK VALIDITY
   - While len(mp) > 2:
     - Decrement mp[arr[low]]
     - If mp[arr[low]] == 0, delete from map
     - Increment low

STEP 4: TRACK MAXIMUM
   - Calculate length = high - low + 1
   - Update ans = max(ans, length)

STEP 5: CONTINUE
   - Increment high
   - Repeat until high reaches end of array

STEP 6: RETURN
   - Return ans as the longest valid subarray length
"""

# ============================================================================
# 🧪 TEST CASES
# ============================================================================
if __name__ == "__main__":
    sol = Solution()
    
    print("=" * 70)
    print("TEST CASE 1")
    print("=" * 70)
    arr1 = [1, 2, 1, 2, 3]
    result1 = sol.totalElements(arr1)
    print(f"Input: {arr1}")
    print(f"Output: {result1}")
    print(f"Expected: 4")
    print(f"Explanation: Longest subarray is [1, 2, 1, 2] with 2 distinct elements")
    print(f"Status: {'✓ PASS' if result1 == 4 else '✗ FAIL'}\n")
    
    print("=" * 70)
    print("TEST CASE 2")
    print("=" * 70)
    arr2 = [1, 2, 3, 4, 5]
    result2 = sol.totalElements(arr2)
    print(f"Input: {arr2}")
    print(f"Output: {result2}")
    print(f"Expected: 2")
    print(f"Explanation: Any two consecutive elements (each has 2 distinct)")
    print(f"Status: {'✓ PASS' if result2 == 2 else '✗ FAIL'}\n")
    
    print("=" * 70)
    print("TEST CASE 3")
    print("=" * 70)
    arr3 = [1, 1, 1, 1]
    result3 = sol.totalElements(arr3)
    print(f"Input: {arr3}")
    print(f"Output: {result3}")
    print(f"Expected: 4")
    print(f"Explanation: Entire array has only 1 distinct element")
    print(f"Status: {'✓ PASS' if result3 == 4 else '✗ FAIL'}\n")
    
    print("=" * 70)
    print("TEST CASE 4")
    print("=" * 70)
    arr4 = [0, 1, 2, 1, 0, 1, 3]
    result4 = sol.totalElements(arr4)
    print(f"Input: {arr4}")
    print(f"Output: {result4}")
    print(f"Expected: 5")
    print(f"Explanation: Longest subarray is [0, 1, 2, 1, 0] with 2 distinct (0, 1)")
    print(f"Status: {'✓ PASS' if result4 == 5 else '✗ FAIL'}\n")
    
    print("=" * 70)
    print("TEST CASE 5 (Edge Case)")
    print("=" * 70)
    arr5 = [1, 2]
    result5 = sol.totalElements(arr5)
    print(f"Input: {arr5}")
    print(f"Output: {result5}")
    print(f"Expected: 2")
    print(f"Explanation: Array with exactly 2 distinct elements")
    print(f"Status: {'✓ PASS' if result5 == 2 else '✗ FAIL'}\n")
    
    print("=" * 70)
    print("TEST CASE 6 (Edge Case)")
    print("=" * 70)
    arr6 = [1]
    result6 = sol.totalElements(arr6)
    print(f"Input: {arr6}")
    print(f"Output: {result6}")
    print(f"Expected: 1")
    print(f"Explanation: Single element (1 distinct)")
    print(f"Status: {'✓ PASS' if result6 == 1 else '✗ FAIL'}\n")
