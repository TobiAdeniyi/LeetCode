/*
Runtime: 8 ms, faster than 67.22% of C++ online submissions for Implement strStr().
Memory Usage: 6.8 MB, less than 71.86% of C++ online submissions for Implement strStr().
*/

class Solution {
public:
    int strStr(string haystack, string needle) {
        if (haystack.find(needle) != std::string::npos) {
            return haystack.find(needle);
        } else {
            return -1;
        }
    }
};