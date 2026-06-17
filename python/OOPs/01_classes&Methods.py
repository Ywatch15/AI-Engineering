'''
self._ -> is used for protected view
self.__ -> is used for private view
self. -> is used for public view
'''

class Car():

    def __init__(self,windows, doors, engineType):
        self.windows=windows
        self.doors=doors
        self.engineType = engineType
    def drive():
        print("The person drives the {} car.".format(self.engineType))


car=Car(4,4,"cng")
print(car.engineType)
