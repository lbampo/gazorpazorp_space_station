from expedition_class import *

class Cargo(Expedition):
    def __init__(self, destination, weight, cargo, spaceship = '', origin = 'Gazorpazorp Station'):
        super().__init__(destination, spaceship, origin)
        self.weight = weight
        self.cargo = cargo



    def pay_tariffs(self):
        return self.weight * 1.12 # 1.12 is tariff

    def expo_details(self):
        cargo_details = {
            'origin' : self.__origin,
            'destination': self.__destination,
            'spaceship': self.__spaceship,
            'pass_list': self.__passenger_list,
            'weight': self.weight,
            'cargo': self.cargo
        }
        return cargo_details


cargo_examp = Cargo('Lis', 1345, 'Bananas', 'Tardis')

print(cargo_examp.expo_details())


