class Car():
    def __new__(self, windows,doors,engineType):
        print("The object has started getting initialized")
    def __init__(self,windows, doors, engineType):
        self.windows=windows
        self.doors=doors
        self.engineType = engineType
    def __str__(self):
        return "The car has {} windows, {} doors and runs on {} engine.".format(self.windows,self.doors,self.engineType)
    def __sizeof__(self):
        return "The object size is {} bytes".format(self.__sizeof__())
    def drive(self):
        print("The person drives the {} car.".format(self.engineType))


c=Car(4,5,"Diesel")
print(c)

print(c.__sizeof__())
# dir(c)