# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

class Solution:
    def minPartitions(self, n: str) -> int:
        for i in range(9, -1, -1):
            if str(i) in n:
                return int(i)