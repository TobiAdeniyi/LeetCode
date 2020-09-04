/*
Runtime: 8 ms, faster than 93.32% of C++ online submissions for Search Insert Position.
Memory Usage: 9.7 MB, less than 54.32% of C++ online submissions for Search Insert Position.
*/

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int i = 0;
        while (nums[i] < target) {
            i ++;
            if (i == nums.size()) break;     
        }
        return i;
    } 
};