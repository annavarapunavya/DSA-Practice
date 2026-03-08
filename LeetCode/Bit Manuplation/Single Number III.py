/*
Problem: Two Sum
Platform: LeetCode
Link: https://leetcode.com/problems/single-number-iii/
*/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor =0
        for num in nums:
            xor ^= num
        rb = (xor) & (-xor)
        x,y=0,0
        for num in nums:
            if num & rb ==0:
                x=x^num
            else:
                y=y^num
        return [x,y]
        
