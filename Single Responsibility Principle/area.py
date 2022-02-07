class area:
    def __init__(self):
        self._width=None
        self._height=None
    
    def get_width(self):
        return self._width

    def set_width(self,width):
        self._width=width

    def get_height(self):
        return self._height

    def set_height(self,height):
        self._height=height

class rectangle:
    def __init__(self,width,height):
        self._ob=area()
        self._ob.set_width(width)
        self._ob.set_height(height)

    def cal_area(self):
        return self._ob.get_width()*self._ob.get_height()

class square:
    def __init__(self,width,height):
        self._ob=area()
        self._ob.set_width(width)
        self._ob.set_height(height)

    def cal_area(self):
        return self._ob.get_width()*self._ob.get_height()

dim=rectangle(10,6)
print(dim.cal_area())

side=square(6,6)
print(side.cal_area())

