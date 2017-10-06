# Create a new class called Bike with the following properties/attributes: price, max_speed, miles
class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

# Add the following functions to this class: displayInfo(), ride(), reverse()
    def displayInfo(self):
        print "Price: ", self.price, "Max speed: ", self.max_speed, " Total miles: ", self.miles

    def ride(self):
        self.miles += 10
        print "Riding ", self.miles

    def reverse(self):
        if self.miles > 0:
            self.miles -= 5
            print "Reversing ", self.miles
            return self
# Create 3 instances of the Bike class.
bike1 = Bike(200, "25mph")
bike2 = Bike(300, "40mph")
bike3 = Bike(50, "10mph")
# Have the first instance ride three times, reverse once and have it displayInfo().
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()
# Have the second instance ride twice, reverse twice and have it displayInfo().
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()
#  Have the third instance reverse three times and displayInfo().
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()

# What would you do to prevent the instance from having negative miles?
    # if self.miles > 0
# Which methods can return self in order to allow chaining methods?
    # ride and reverse