class Points(object):
    def __init__(self,x=0,y=0):
        self.x= x
        self.y= y
    def __add__(self, other):
        newpoint=Points()
        if isinstance(other, Points):
            newpoint.x = self.x+other.x
            newpoint.y = self.y+other.y
            return newpoint
        elif isinstance(other, tuple):
            newpoint.x = self.x + other[0]
            newpoint.y = self.y +other[1]
            return newpoint
    def __str__(self):
        return '%s,%s' %(self.x,self.y)

point1 = Points(5,6)
point2 = Points(7,8)
print(point1+point2)
