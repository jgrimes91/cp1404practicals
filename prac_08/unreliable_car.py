from prac_08.car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        test_drive = randint(0, 100)
        if test_drive >= self.reliability:
            distance = 0

        distance_driven = super().drive(distance)
        return distance_driven