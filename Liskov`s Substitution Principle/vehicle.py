import time

class vehicle:
    def __init__(self, name, speed):
        self._name=name
        self._speed=speed

    def get_name(self):
        return f"The vehicle name is {self._name}"

    def get_speed(self):
        return f"Speed is {self._speed}"

class vehicle_without_engine(vehicle):
    def start_moving(self):
        return 0
        

class vehicle_with_engine(vehicle):
    def start_engine(self):
        startTime=time.time()
        #Ignition time
        for i in range(1000):
            for j in range(1000):
                continue
        endTime=time.time()
        return endTime-startTime
    
        

class car(vehicle_with_engine):
    def start_engine(self):
        return super().start_engine()

class bicycle(vehicle_without_engine):
    def start_moving(self):
        return super().start_moving()


ob=car("Mercedes",120)
print("Car starts in :","{0:.3f}".format(ob.start_engine()),"seconds")