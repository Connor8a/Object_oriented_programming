from Vehicle import Vehicle


bug_object = Vehicle("beetle", "yellow", 4, 1) #object of cehicle class -- instnce of vechile class
turtle_object = Vehicle("turtlebot", "green", 2, 5)
rover_object = Vehicle("rover", "purple", 4, 25)

bug_object.print_details()
turtle_object.print_details()
rover_object.print_details()

bug_object.paint_vechile("blue")
bug_object.print_details()
