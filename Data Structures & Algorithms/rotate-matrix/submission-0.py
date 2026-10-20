class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows=len(matrix)
        cols=len(matrix[0])
        t=0
        b=rows-1
        while t<b:
            matrix[t],matrix[b]=matrix[b],matrix[t]
            t+=1
            b-=1
        for i in range(rows):
            c=0
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i], matrix[i][j]
        

        
        