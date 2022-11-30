class Vehicle:
    
    def __init__(self, nm, color, num_wheels, speed):
        self.name = nm
        self.color = color
        self.num_wheels = num_wheels
        self.speed = speed



bug_object = Vehicle("beetle", "yellow", 4, 1) #object of cehicle class -- instnce of vechile class
turtle_object = Vehicle("turtlebot", "green", 2, 5)
rover_object = Vehicle("rover", "purple", 4, 25)

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
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()

print('This vehicle is',bug_object.color, 
'and is able to drive', bug_object.speed, 'mph')
print('This vehicle is',turtle_object.color, 
'and is able to drive', turtle_object.speed, 'mph')
print('This vehicle is',rover_object.color, 
'and is able to drive', rover_object.speed, 'mph')


