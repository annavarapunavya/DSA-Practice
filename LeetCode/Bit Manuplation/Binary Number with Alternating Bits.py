/*
Problem: Binary NUmber with Alternative Bits
Platform: LeetCode
Link:https://leetcode.com/problems/binary-number-with-alternating-bits/
*/
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_num = bin(n)[2:]
        
        for i in range(len(bin_num) - 1):
            if bin_num[i] == bin_num[i + 1]:
                return False
                
        return True
