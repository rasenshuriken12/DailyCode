class Solution {
  public:
    int longestSubarray(vector<int> &arr, int k) {
        // Code here
        int n = arr.size();
        unordered_map<int,int>m;
        int sum = 0;
        int ans = 0;
        
        for(int i=0;i<n;i++){
            
            if(arr[i]<=k)sum-=1;
            else sum+=1;
            
            if(sum>0)ans=i+1;
            else{
                int num = -((abs(sum)+1));
                if(m.count(num))ans = max(ans,i-m[num]);
            }
            
            if(m.count(sum)==0)m[sum]=i;
            
        }
        
        return ans;
    }
};

// ═══════════════════════════════════════════════════════════════
// APPROACH 2: Direct Count Difference with HashMap
// ═══════════════════════════════════════════════════════════════
/*
🔷 Alternative Intuition

Instead of encoding as +1/-1 and maintaining prefix sum,
directly track two counters:

  gtk (greater than k) = count of elements > k
  lek (less or equal to k) = count of elements ≤ k
  
The difference (gtk - lek) at each position tells us:
  - If positive: more elements > k than ≤ k (satisfies majority)
  - If we've seen (diff - 1) before: removing that segment makes current segment valid

🔹 Key Observation

If at index j we have diff = gtk - lek,
and we previously had diff-1 at some index i,
then in subarray (i+1)...j:
  - Number of gtk elements = gtk_j - gtk_i = X
  - Number of lek elements = lek_j - lek_i = X - 1
  - So: (gtk - lek) at this subarray = X - (X-1) = 1 > 0 ✓

This subarray has majority > k!

🔹 HashMap Strategy
- Store FIRST occurrence of each diff value
- When we see diff, check if (diff - 1) exists
  - If yes: valid subarray found, update length
  - If no: entire prefix might be valid (if diff > 0)

🔷 Dry Run (Example)
arr = [1, 2, 3, 4]
k = 2

Index  arr[i]  gtk>k?   gtk   lek   diff   map[diff-1]?   Action
  -1                     0     0      0     -             map[0]=-1
   0      1      NO      0     1     -1     map[-2]?NO     -
   1      2      NO      0     2     -2     map[-3]?NO     -
   2      3      YES     1     2     -1     map[-2]exists!  len=2-(-1)=3 ✓ 
   3      4      YES     2     2      0     diff-1=-1       diff≥0: len=3+1=4 ✓

Answer: 4

🔷 Key Differences from Approach 1

Approach 1 (Prefix Sum):
  - Encodes as +1/-1, maintains prefix sum
  - Reduces to: "longest subarray with sum > 0"
  - Checks sum > 0 directly

Approach 2 (Direct Count):
  - Tracks actual counts of gtk and lek
  - Maintains difference dynamically
  - More intuitive for understanding the majority concept
  - Same time/space complexity

Both approaches are equivalent mathematically!
*/

class Solution2 {
  public:
    int longestSubarray(vector<int> &arr, int k) {
        unordered_map<int, int> mp;
        
        int maxLen = 0;
        int n = arr.size();
        int gtk = 0;  // count of elements > k
        int lek = 0;  // count of elements <= k
        
        for(int j = 0; j < n; j++){
            if(arr[j] > k) gtk++;
            else lek++;
            
            int diff = gtk - lek;
            
            // Check if (diff - 1) exists in our map
            // This means: we can form a valid subarray by skipping that segment
            if((diff - 1) < 0 && mp.count(diff - 1)){
                maxLen = max(maxLen, j - mp[diff - 1]);
            }
            else {
                // If (diff - 1) >= 0, it means diff > 0
                // So entire prefix [0...j] has majority > k
                if((diff - 1) >= 0){
                    maxLen = max(maxLen, j + 1);
                }
            }
            
            // Store first occurrence of this diff value
            if(!mp.count(diff)){
                mp[diff] = j;
            }
        }
        
        return maxLen;
    }
};

/* 
═══════════════════════════════════════════════════════════════
COMPLEXITY ANALYSIS (Both Approaches)
═══════════════════════════════════════════════════════════════

Time Complexity: O(n)
  - Single pass through the entire array
  - HashMap insert/lookup operations: O(1) average case
  - Total: O(n) where n is array length

Space Complexity: O(n)
  - HashMap stores at most n unique difference/prefix sum values
  - Worst case: all prefix sum values are distinct
  - Total additional space: O(n)

Why Not O(1) Space?
  - We cannot solve in O(1) space because:
  - We need to remember previous diff values
  - Cannot use sliding window (contiguous window approach doesn't work here)
  - HashMap is essential to track non-contiguous jumps

═══════════════════════════════════════════════════════════════
*/