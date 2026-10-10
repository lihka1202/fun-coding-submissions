class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxNumberOfOnes = 0, currentCounter = 0;
        for (int num : nums) {
            if (num == 1) {
                currentCounter += 1;
            } else {
                currentCounter = 0;
            }
            maxNumberOfOnes = max(maxNumberOfOnes, currentCounter);
        }
        return maxNumberOfOnes;
    }
};