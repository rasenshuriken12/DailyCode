class Solution {
  public:
    int maxOnes(vector<int>& arr, int k) {
        queue <int> onesPlaced;
        int maxSize=0,initial=0;
        
        for(int i=0;i<arr.size();i++){
            
            if(arr[i]==0){
                
                onesPlaced.push(i);
                
                if(k!=0) k--;
                
                else{
                int prev=onesPlaced.front();    
                onesPlaced.pop();
                initial=prev+1;
                }
            }
            
            maxSize=max(maxSize,(i-initial+1));
        }
        return maxSize;
    }
};