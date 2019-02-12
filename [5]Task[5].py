class Point(object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return '%d,%d' %(self.x,self.y)

    def __add__(self, other):
        newx = self.x+other.x
        newy = self.y+other.y
        newpoint=Point(newx,newy)
        return newpoint

point = Point(10,20)
point1 = Point(30,40)
print(point+point1)
