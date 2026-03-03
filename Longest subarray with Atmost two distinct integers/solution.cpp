class Solution {
  public:
    int totalElements(vector<int> &arr) {
        // code here
        int n = arr.size();
        int i = 0;
        int maxi = 0;
        map <int, int> mpp;
        for (int j = 0; j < n; j++){
            mpp[arr[j]]++;
            while (mpp.size() > 2){
                mpp[arr[i]]--;
                if (mpp[arr[i]] == 0)
                    mpp.erase(arr[i]);
                i++;
            }
            maxi = max(maxi, j - i + 1);
        }
        return maxi;
    }
};