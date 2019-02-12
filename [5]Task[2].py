#This is the code
class point():
    def __init__(self):
        self.x=0
        self.y=0
    def distance_between_points(self):
        return abs(self.x-self.y)
class rectangle():
    def __init__(self):
        self.width=100
        self.height=200
        self.corner=point().distance_between_points()
    def center_rectangle(self):
        dwidth = (self.width-point().x)/2
        dheight=(self.height-point().y)/2
        t = [dwidth,dheight]
        print(tuple(t))
    def find_center():
    print(rectangle().center_rectangle())
    def move_rectangle(dx,dy)
        self.width+=dx
	self.height+=dy
move_rectangle(50,100)
find_center()
