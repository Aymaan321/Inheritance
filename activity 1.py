class vehicle():
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class bus(vehicle):
    pass

school_bus = bus("school_volvo", 150, 20)
print(f"Vehicle name: {school_bus.name} \nMax speed: {school_bus.max_speed} \nMileage: {school_bus.mileage")
