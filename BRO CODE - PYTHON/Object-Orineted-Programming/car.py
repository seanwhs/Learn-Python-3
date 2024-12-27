# car.py
class Car:
    def __init__(self, model, year, colour, is_for_sale):
        self.model = model
        self.year = year
        self.colour = colour
        self.is_for_sale = is_for_sale

    def drive(self):
        print(f'You drive the {self.colour} {self.model}')

    def stop(self):
        print(f'You stop the {self.colour} {self.model}')

    def describe(self):
        print(f'Decsription:: {self.year}, {self.model}, {self.colour}, For Sale: {self.is_for_sale}')