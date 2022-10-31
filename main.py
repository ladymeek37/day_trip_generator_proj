destinations = ["Costa Rica", "Alaska", "Paris", "Brasil", "Oregon"]
restaurants = ["A local cafe", "In n out", "Chipotle", "Canes", "Sambazon"]
transportation = ["Skateboard", "Bus", "Boat", "Train", "Limousine"]
entertainment = ["Jack Johnson Concert", "Circus", "Fishing", "Line Dancing", "Sky Diving"]


def trip_generator():

    import random
    print ("Destination:" + random.choice(destinations))

    import random
    print ("Restaurant:" + random.choice(restaurants))

    import random
    print ("Transportation:" + random.choice(transportation))

    import random
    print ("Entertainment:" + random.choice(entertainment))

    print (" ")

print (" ")

print ("Random Trip Generator!")

print (" ")

trip_generator()

user_input = input("Are you satisfied with your trip? Yes or No   ")
while user_input == "No":
    print("")
    print("New Trip:")
    print("")
    trip_generator()
    user_input = input("Are you satisfied with your trip? Yes or No   ")
    if user_input == "Yes":
     print("Your trip selection is complete!")
     print()