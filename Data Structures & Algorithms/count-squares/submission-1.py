class CountSquares:

    def __init__(self):
        self.H=defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.H[tuple(point)]+=1
    def count(self, point: List[int]) -> int:
        pointx,pointy=point
        diagx,diagy=-1,-1
        count=0
        for px, py in list(self.H):
            if abs(pointx-px)==abs(pointy-py) and pointx!=px and pointy!=py:
                diagx,diagy=px,py
                #while self.H[(diagx,py)]>=1 and self.H[(px,diagy)]>=1:
                count+=self.H[(diagx,diagy)]*self.H[(diagx,pointy)]*self.H[(pointx,diagy)]
                    #multiplying frequencies isntead of premanently modifying frequency map

        if diagx==-1:
            return 0
        return count
        


        
