# Spaceship should have:

class Spaceship():

    def __init__(self, captain, name, intergalactic_signature ):
        self.captain = captain
        self.__name = name
        self.__signature = intergalactic_signature



    def identify(self):
        return self.__signature

    def change_name(self, name):
        self.__name = name


# Captain
# Name(ID)
# Intergalactic_signature