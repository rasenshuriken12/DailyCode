class Solution {
  public:
    int minCost(vector<int>& heights, vector<int>& cost) {
        // code here
        int low =INT_MAX;
        int high = INT_MIN;
        int n = (int)heights.size();
        for(auto it:heights)
        {
            low = min(low,it);
            high = max(high,it);
        }
        
        auto f = [&](int mid)->long long{
            
            long long ans = 0;
            for(int i=0;i<n;i++)
            {
                ans+=abs(mid-heights[i])*1LL*cost[i]*1LL;
            }
            return ans;
        };
        long long minm_cost = LLONG_MAX;
        while(low<=high)
        {
            int mid = (low+high)/2;
            
            long long cost1 = f(mid);
            long long cost2 = (mid==high)?LLONG_MAX:f(mid+1);
            
            if(cost1<=cost2)
            {
                minm_cost = min(minm_cost,cost1);
                high = mid-1;
            }
            else
            {
                low = mid+1;
            }
        }
        
        return minm_cost;
        
    }
};