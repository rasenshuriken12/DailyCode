class Solution {
  public:
    int maxSubarrayXOR(vector<int>& arr, int k) {
        int n = arr.size();
        
        // Calculate XOR of first window
        int currentXor = 0;
        for(int i = 0; i < k; i++) {
            currentXor ^= arr[i];
        }
        
        int maxXor = currentXor;
        
        // Slide the window and update XOR
        for(int i = k; i < n; i++) {
            // Remove the leftmost element of previous window
            currentXor ^= arr[i - k];
            // Add the new rightmost element
            currentXor ^= arr[i];
            maxXor = max(maxXor, currentXor);
        }
        
        return maxXor;
    }
};