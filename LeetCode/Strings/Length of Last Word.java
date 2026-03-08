/*
Problem: Length of Last Word
Platform: LeetCode
Link: https://leetcode.com/problems/length-of-last-word/
*/


import java.util.*;
class Solution {
    public int lengthOfLastWord(String s) {
        String x = null;
        StringTokenizer st = new StringTokenizer(s);
        while(st.hasMoreTokens())
        {
            x = st.nextToken();
        }
        return x.length();
    }
}
