class Vehicle:
    pass

bug_object = Vehicle() #object of cehicle class -- instnce of vechile class
turtle_object = Vehicle()
rover_object = Vehicle()

bug_object.color = "yellow"
bug_object.num_wheels = 4
# speed 1 mph
bug_object.speed = 1


turtle_object.color = "green"
turtle_object.num_wheels = 2
# speed 5 mph
turtle_object.speed = 5


rover_object.color = "purple"
rover_object.num_wheels = 4
# speed 25 mph 
rover_object.speed = 25

print(bug_object)
print(turtle_object)
print(rover_object)

