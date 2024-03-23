class Car():

    def __init__(self, Model, Serial):
        self.Model = Model
        self.Serial = Serial

    def print(self):
        print(f"the model is {self.Model} and the Serial Number is {self.Serial}")



akrem = Car("Partner", 108)
print(type(akrem))
akrem.print()