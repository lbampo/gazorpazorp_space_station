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
        # Send a dictionary with
            # Origin
            # Destination
            # Spaceship
            # Passengers
        expo_details_dict = {
            'origin' : self.__origin,
            'destination': self.__destination,
            'spaceship': self.__spaceship,
            'pass_list': self.__passenger_list
        }

        return expo_details_dict
# A origin ( always gazorpazorp space station)
# A destination
# Space ship assigned
# List of passengers