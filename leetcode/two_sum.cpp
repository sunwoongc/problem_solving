using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> TargetSum;
        
        for (int i = 0; i < nums.size(); i++){
            auto it = TargetSum.find(target-nums[i]);
            if (it != TargetSum.end() && it->second != i){
                return {it->second, i};
            }
            TargetSum[nums[i]] = i;
        }
        
        return {};
    }
};
