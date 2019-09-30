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
ship_4 = Spaceship("Cage", "Nicoloaus Excelsior", "CAGE1776")

# Generate 3 expeditions

expo_1 = Expedition('Mars', ship_1)
expo_2 = Expedition('Death Star', ship_2)
expo_3 = Expedition('Nowhere', ship_3)


expo_list = []
expo_list.append(expo_1)
expo_list.append(expo_2)
expo_list.append(expo_3)


expo_3.assign_spaceship(ship_4)


expo_1.add_pass_expo(passenger_1)
expo_1.add_pass_expo(passenger_2)

expo_2.add_pass_expo(passenger_3)
expo_2.add_pass_expo(passenger_4)

expo_3.add_pass_expo(passenger_5)
expo_3.add_pass_expo(passenger_6)

# print(expo_1.expo_details())


    # keep list of generated expeditions (add to empty listy of expeditions)
    # Assign spaceship to each one
        # Should be able to assign pon creation of object
                    #or
        # Should be able to assign post-facto

    #Assign to each expedition 2 passengers (append)

    # Iterate over list of expeditions and print
for list in expo_list:
    for key in list.expo_details():
        print(key, list.expo_details() [key])


        # Iterate over list of passenger object and print out passenger details


# Create while loop here

# * As a user I can create passengers
# * As a user i can list all expeditions
# * As a user i can add passengers to an expedition#
# * As a user i can list passengers in expedition

for expedition in expo_list:
    print(expedition)

    print(expedition.expo_details()['origin'], expedition.expo_details()['destinbation'], expedition.expo_details()['ship'].identify)