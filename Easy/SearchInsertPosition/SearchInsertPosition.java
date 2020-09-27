// Runtime: 0 ms, faster than 100.00% of Java online submissions for Search Insert Position.
// Memory Usage: 39 MB, less than 84.62% of Java online submissions for Search Insert Position.

class Solution {
    public int searchInsert(int[] nums, int target) {
        int i = 0;
        while (nums[i] < target) {
            i ++;
            if (i == nums.length) break;
        }
        return i;
    }
}