from prac_08.unreliable_car import UnreliableCar

def main():
    car_one = UnreliableCar("Alright", 100, 90)
    car_two = UnreliableCar("Dodge", 100, 9)

    for i in range(1, 10):
        print("Testing cars, {}km".format(i))
        print("{:10} drove {:2}km".format(car_one.name, car_one.drive(i)))
        print("{:10} drove {:2}km".format(car_two.name, car_two.drive(i)))

    print(car_one)
    print(car_two)


main()