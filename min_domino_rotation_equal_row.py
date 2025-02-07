class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        length = len(tops)
        re = self.check(tops, bottoms, tops[0])
        if re != -1:
            return re
        else:
            return self.check(tops, bottoms, bottoms[0])

    def check(self, tops, bottoms, target):

        tRot = 0
        bRot = 0
        for i in range(len(tops)):
            if tops[i] != target and bottoms[i] != target:
                return -1
            if tops[i] != target:
                tRot += 1
            if bottoms[i] != target:
                bRot += 1
        return min(tRot, bRot)


# time complexity is O(n)
# space complexity is O(1)
