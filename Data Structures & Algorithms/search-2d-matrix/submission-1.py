class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        lenx=len(matrix[0])
        leny=len(matrix)
        r=lenx*leny-1
        while l<=r:
            mid=(l+r)//2
            y=mid//lenx
            x=mid%lenx
            if matrix[y][x]==target:
                return True
            elif matrix[y][x]>target:
                r=mid-1
            if matrix[y][x]<target:
                l=mid+1
        return False
