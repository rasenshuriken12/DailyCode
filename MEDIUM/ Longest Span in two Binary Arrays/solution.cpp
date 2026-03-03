class Solution {
  public:
    int equalSumSpan(vector<int> &a1, vector<int> &a2) {
        // code here
        int n = a1.size(), ans = 0;
        unordered_map<int, int> mp;
        mp[0] = -1;
        for(int i = 0, s = 0; i < n; i++) {
            s += (a1[i] - a2[i]);
            if(mp.count(s) != 0) ans = max(ans, i - mp[s]);
            if(mp.count(s) == 0) mp[s] = i;
        }
        return ans;
    }
};

// ═══════════════════════════════════════════════════════════════
// APPROACH 2: Hash Map + Prefix Sum Difference
// ═══════════════════════════════════════════════════════════════

🔷 Intuition 
We need to find the longest span (i, j) such that:

Sum of a1[i…j] = Sum of a2[i…j]

A brute force way would be:

Check all subarrays

Compare their sums

But that would take O(n²) time — too slow.

So we think smarter.

🔹 Key Observation
If:

Sum(a1[i…j]) = Sum(a2[i…j])

Then:

(prefix1[j] − prefix1[i−1]) = (prefix2[j] − prefix2[i−1])

Rearranging:

(prefix1[j] − prefix2[j]) = (prefix1[i−1] − prefix2[i−1])

So if the difference of prefix sums is same at two indices,
then the subarray between them has equal sum.

🔹 Trick
At every index calculate:

diff = prefix1 − prefix2

If the same diff appears again at some later index,
then the elements between those two indices form a valid span.

To do this efficiently:

Use a hashmap

Store first occurrence of each diff

When diff repeats → update max length

🔷 Dry Run (Example 1)
a1 = [0,1,0,0,0,0]
a2 = [1,0,1,0,0,1]

Initialize:

prefix1 = 0
prefix2 = 0
maxLen = 0
mp[0] = -1 (important: handles span starting from index 0)

i = 0
prefix1 = 0
prefix2 = 1
diff = -1

Not in map → store
mp[-1] = 0

i = 1
prefix1 = 1
prefix2 = 1
diff = 0

0 already in map at index -1

length = 1 - (-1) = 2
maxLen = 2

i = 2
prefix1 = 1
prefix2 = 2
diff = -1

Seen before at index 0

length = 2 - 0 = 2

i = 3
prefix1 = 1
prefix2 = 2
diff = -1

Seen at 0

length = 3 - 0 = 3
maxLen = 3

i = 4
prefix1 = 1
prefix2 = 2
diff = -1

Seen at 0

length = 4 - 0 = 4
maxLen = 4

i = 5
prefix1 = 1
prefix2 = 3
diff = -2

Not in map → store
mp[-2] = 5

Final Answer:

maxLen = 4 ✔

// ═══════════════════════════════════════════════════════════════
// COMPLEXITY ANALYSIS
// ═══════════════════════════════════════════════════════════════
// Time Complexity: O(n)
//   - Single pass through arrays
//   - HashMap operations: O(1) average case
//
// Space Complexity: O(n)
//   - HashMap stores at most n unique prefix sum differences
//   - Worst case: all differences are unique
// ═══════════════════════════════════════════════════════════════

