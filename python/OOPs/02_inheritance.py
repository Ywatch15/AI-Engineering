class Car():
    def __init__(self,windows, doors, engineType):
        self.windows=windows
        self.doors=doors
        self.engineType = engineType
    def drive(self):
        print("The person drives the {} car.".format(self.engineType))


class Audi(Car):
    def __init__(self, windows, doors, engineType, enableAI):
        super().__init__(windows, doors, engineType)
        self.enableAI=enableAI

    def selfDriving(self):
        print("It supports self-driving")


audi1=Audi(5,5,"petrol", True)
print(audi1.windows)