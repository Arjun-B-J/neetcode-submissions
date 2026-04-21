class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)]+=1

    def count(self, point: List[int]) -> int:
        x,y = point
        count=0
        for (px,py),n in self.points.items():
            if abs(x-px) == abs(y-py) and px!=x and py!=y:
                if (x,py) in self.points and (px,y) in self.points:
                    count+= (n*self.points[(x,py)]*self.points[(px,y)]) 
        return count
