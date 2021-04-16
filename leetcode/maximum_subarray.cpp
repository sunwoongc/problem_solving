// class Solution {
// public:
//     int maxSubArray(vector<int>& nums) {
        
//         const int size = nums.size();
//         int curSum = nums[0];
//         int ans = nums[0];
        
//         for (int it = 1; it < size; it++){
//             curSum = max(nums[it], curSum+nums[it]);
//             ans = max(curSum,ans);
//             }

//         return ans;
//     }
    
// };
// constantly update the maximum value.

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        const int size = nums.size();
        int curSum = 0;
        int ans = nums[0];
        
        for (int it = 0; it < size; it++){
            if (curSum < 0){
                curSum = 0;
            }
            
            curSum += nums[it];
            ans = max(curSum,ans);
        }
        
        return ans;
    }
};
// realize that we don't need to add a negative value.
