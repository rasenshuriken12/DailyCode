🧠 Problem Intuition — What are we really maximizing?
We must maximize:

R= ∑  ​i×arr[i]
But we are allowed to rotate the array any number of times.

A brute force way is: rotate → compute → rotate → compute…
That costs O(n²) ❌ (not acceptable).

So the real question is:

Can we compute the next rotation’s value from the previous one in O(1)?

Yes. That’s the key insight.

🔍 Observe the pattern after one rotation
Let:

arrSum = arr[0] + arr[1] + ... + arr[n-1]

R0 = 0*arr[0] + 1*arr[1] + ... + (n-1)*arr[n-1]

After one clockwise rotation, last element comes to front.

New array:

 
[arr[n-1], arr[0], arr[1], ..., arr[n-2]]
New value R1R1R1:

R1=0⋅arr[n−1]+1⋅arr[0]+2⋅arr[1]+...+(n−1)⋅arr[n−2]R1 = 0 \cdot arr[n-1] + 1 \cdot arr[0] + 2 \cdot arr[1] + ... + (n-1) \cdot arr[n-2]R1=0⋅arr[n−1]+1⋅arr[0]+2⋅arr[1]+...+(n−1)⋅arr[n−2]

Rewriting this cleverly using R0R0R0:

R1=R0+arrSum−n⋅arr[n−1]R1 = R0 + arrSum - n \cdot arr[n-1]R1=R0+arrSum−n⋅arr[n−1]

✨ This is the breakthrough.

🔁 General Recurrence Relation
For every rotation:

Rk=Rk−1+arrSum−n⋅arr[n−k]R_k = R_{k-1} + arrSum - n \cdot arr[n-k]Rk​=Rk−1​+arrSum−n⋅arr[n−k]

This lets us compute each rotation in O(1) time.

Total complexity → O(n) ✅
Space → O(1) ✅

📊 Visual Walkthrough
Example: arr = [3, 1, 2, 8]

https://youcademy.org/juggling-dolphin-algorithm-for-array-rotation/one-set-loop.png
https://youcademy.org/rotate-elements-in-an-array/circular-array.png
Rotation	Configuration	Value of R
R0	[3, 1, 2, 8]	29
R1	[8, 3, 1, 2]	11
R2	[2, 8, 3, 1]	17
R3	[1, 2, 8, 3]	27
We never recompute from scratch.
We use the recurrence every time.

🚀 Implementation (Optimal Approach)
 
class Solution {
public:
    int maxSum(vector<int> &arr) {
        int n = arr.size();
        
        long long arrSum = 0;
        long long currVal = 0;
        
        for(int i = 0; i < n; i++) {
            arrSum += arr[i];
            currVal += (long long)i * arr[i];
        }
        
        long long res = currVal;
        
        for(int k = 1; k < n; k++) {
            currVal = currVal + arrSum - (long long)n * arr[n - k];
            res = max(res, currVal);
        }
        
        return res;
    }
};
 

💡 Why this works (core insight)
When we rotate:

Every element’s index increases by +1

Except the last element → jumps from index n-1 to 0

That single jump is why we subtract n * lastElement.

❌ Why naive rotation fails
Rotating array each time → O(n)

Recomputing sum each time → O(n)

Total → O(n²)

This problem is designed to test whether you see the mathematical pattern, not rotation simulation.

🏁 Final Takeaway
This is a classic example where:

Understanding index behavior after rotation leads to an O(n) mathematical solution instead of brute force simulation.

That recurrence relation is the entire game changer.