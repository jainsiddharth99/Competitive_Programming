class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        areaA = (C - A) * (D - B)
        areaB = (G - E) * (H - F)
        l = max(0, min(C, G) - max(A, E))
        h = max(0, min(D, H) - max(B, F))
        return areaA + areaB - l * h
