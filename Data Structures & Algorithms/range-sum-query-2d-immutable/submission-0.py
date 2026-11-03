class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        #self.total=0
        rows=len(matrix)
        cols=len(matrix[0])
        self.prefix=[[0]*(cols+1) for _ in range(rows)]
        #self.post=[[0]*len(matrix[0]) for _ in range(len(matrix))]
        
        for r in range(rows):
            #self.total+=matrix[r][0]
            for c in range(1,cols+1):
                self.prefix[r][c]=self.prefix[r][c-1]+matrix[r][c-1]
                #post_i=cols-c-1
                #self.post[r][post_i]+=matrix[r][post_i+1]
                #self.total+=matrix[r][c]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res=0
        for r in range(row1,row2+1):
            res+=(self.prefix[r][col2+1]-self.prefix[r][col1])
            

        return res
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)