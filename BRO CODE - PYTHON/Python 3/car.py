
class Car:
    def __init__(self, model, year, colour, for_sale):
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale

    def drive(self):
        print(f'Driving {self.colour} {self.model}')

    def stop(self):
        print(f'Stopping {self.colour} {self.model}')

    def describe(self):
        print(f'Description: {self.year}, {self.model}, {self.colour}')