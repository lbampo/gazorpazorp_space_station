#Expedition details should have:
class Expedition():

    def __init__(self, destination, spaceship = '', origin = 'Gazorpazorp Space station'):
        self.__destination = destination
        self.__origin = origin
        self.__spaceship = spaceship
        self.__passenger_list = []


    def assign_spaceship(self, new_ship):
        self.__spaceship = new_ship

    def expo_details(self):
        expo_details_dict = {
            'origin' : self.__origin,
            'destination': self.__destination,
            'spaceship': self.__spaceship,
            'pass_list': self.__passenger_list

        }

        return expo_details_dict

    def add_pass_expo(self, passenger):
        if self.__passenger_list.append(passenger):
            return True
        else:
            return False

    def get_destination(self):
        return self.__destination

    def get_origin(self):
        return self.__origin

    def get_pass_list(self):
        return self.__passenger_list

    def get_spaceship(self):
        return

    def print_list_passengers(self):
        for passenger in self.get_pass_list():
            print('Name: ' + passenger.name + ',', '')



# A origin ( always gazorpazorp space station)
# A destination
# Space ship assigned
# List of passengers