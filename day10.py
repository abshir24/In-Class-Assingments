class Car:
    topspeed = 250
    location = 0
    
    def printTopSpeed(self):
        print(f'This car has a top speed of {self.topspeed}')
        
    def drive(self):
        self.location += 10
    
    def stop(self):
        print(f'You drove a total of {self.location} miles!')



car1 = Car()

# TASK 1
car1.printTopSpeed()

#Task 2

for i in range(6):
    car1.drive()

car1.stop()




