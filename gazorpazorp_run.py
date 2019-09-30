# Import all classes
from passenger_class import *
from spaceship_class import *
from expedition_class import *



# Create objects

# generate 6 passengers
passenger_1 = Passenger("Poopertings Pooping", "Priopooper", "PP1567")
passenger_2 = Passenger("Hanamanahanamana", "Scoponger", "SC5545")
passenger_3 = Passenger("YsoMAD", "Emowtonpon", "EM5653")
passenger_4 = Passenger("LAPALAPA", "Soundon", "SO3412")
passenger_5 = Passenger("Whodis", "QuestionMaster", "QN5746")
passenger_6 = Passenger("Amy Pond", "Human", "T1")


# generate 3 spaceships
ship_1 = Spaceship('Morgan Freeman', 'GodsPlan', 'GP-1')
ship_2 = Spaceship('Marvel Ous', 'relation-SHIP', 'RS-7')
ship_3 = Spaceship("The DR.", "TARDIS", 'T-1' )

# Generate 3 expeditions

expo_1 = Expedition('Mars', ship_1)
exp0_2 = Expedition('Death Star', ship_2)
expo_3 = Expedition('Nowhere', ship_3)


expo_1.add_pass_expo(passenger_1)
expo_1.add_pass_expo(passenger_2)




    # keep list of generated expeditions (add to empty listy of expeditions)
    # Assign spaceship to each one
        # Should be able to assign pon creation of object
                    #or
        # Should be able to assign post-facto

    #Assign to each expedition 2 passengers (append)

    # Iterate over list of expeditions and print
        # Iterate over list of passenger object and print out passenger details


# Create while loop here

# * As a user I can create passengers
# * As a user i can list all expeditions
# * As a user i can add passengers to an expedition#
# * As a user i can list passengers in expedition

