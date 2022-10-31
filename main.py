import random
from tkinter.messagebox import YES

destinations = ["Costa Rica", "Alaska", "Paris", "Brasil", "Oregon"]
restaurants = ["A local cafe", "In n out", "Chipotle", "Canes", "Sambazon"]
transportation = ["Skateboard", "Bus", "Boat", "Train", "Limousine"]
entertainment = ["A Jack Johnson Concert", "The Circus", "Fishing", "Line Dancing", "Sky Diving"]

random_dest = random.choice(destinations)
random_rest = random.choice(restaurants)
random_trans = random.choice(transportation)
random_entertain = random.choice(entertainment)

def trip_generator():
    print ("Destination:" + random_dest)

    
    print ("Restaurant:" + random_rest)

    
    print ("Transportation:" + random_trans)

    
    print ("Entertainment:" + random_entertain)

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
        random_dest = random.choice(destinations)
        random_rest = random.choice(restaurants)
        random_trans = random.choice(transportation)
        random_entertain = random.choice(entertainment)
        trip_generator()
        user_input = input("Are you satisfied with your trip? Yes or No   ")
if user_input == "Yes":
        print ("")
        print (f"Enjoy your trip to {random_dest}, eating at {random_rest}, traveling by {random_trans}, and enjoying {random_entertain}!")
        print ("")