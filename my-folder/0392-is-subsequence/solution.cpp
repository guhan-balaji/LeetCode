class Solution {
public:
    bool isSubsequence(string s, string t) {
        int s_index = 0;
        for (auto c: t) {
            if (c == s[s_index]) s_index++;
        }
        // if s is subseq of t s_index will be equal to s.size()
        return s_index == s.size();
    }
};
