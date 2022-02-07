class shape:
    def __init__(self,shape):
        self._shape_name=shape

    def get_shape_name(self):
        return self._shape_name

class circle(shape):
    def cal_area(self,radius):
        return (3.14)*radius**2


class square(shape):
    def cal_area(self,side):
        return side*side

cir=circle("circle")
print("The shape is: ",cir.get_shape_name())
print("Area of circle: ",cir.cal_area(3.5))

sq=square("square")
print("The shape is: ",sq.get_shape_name())
print("Area of square: ",sq.cal_area(4))