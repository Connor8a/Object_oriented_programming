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
class Vehicle:

    type = "ground"
    propulsion="battery"
    
    def __init__(self, nm, color, num_wheels, speed):
        self.name = nm
        self.color = color
        self.num_wheels = num_wheels
        self.speed = speed
        #self.type = ground
    def print_details(self):
        print( self.name,'is',self.color, 'and is able to to drive', self.speed, 'mph')
    def paint_vehicle(self, newcolor):
        self.color = newcolor



# drone = Vehicle("droney", "red", 0, 50)

# drone.type = "air"

# print(drone.type)

# print(bug_object.type)


# print('This vehicle is',bug_object.color, 
# 'and is able to drive', bug_object.speed, 'mph')
# print('This vehicle is',turtle_object.color, 
# 'and is able to drive', turtle_object.speed, 'mph')
# print('This vehicle is',rover_object.color, 
# 'and is able to drive', rover_object.speed, 'mph')


