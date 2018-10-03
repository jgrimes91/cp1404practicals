from prac_06.Car import Car

MENU = "Menu: \nd) drive\nr) refuel \nq) quit"

def main():
    print("Let's drive!")
    name = input("Enter your car name: ")
    car = Car(name)
    print(car)
    print(MENU)
    choice = input("Enter your choice: ").lower()
    while choice != "q":
        if choice == "d":
            distance_to_drive = int(input("How many km do you wish to drive? "))
            while distance_to_drive < 0:
                print("Distance must be >= 0")
                distance_to_drive = int(input("How many km do you wish to drive? "))
            distance_driven = car.drive(distance_to_drive)
            print("The car drove {}km".format(distance_driven), end="")
            if car.fuel == 0:
                print(" and ran out of fuel.", end="")
                print(".")
            print()
            print(car)
            print(MENU)
        elif choice == "r":
            refuel = int(input("How many units do you want to add to the car?"))
            while refuel < 0:
                print("Fuel must be > 0")
                refuel = int(input("How many units do you want to add to the car?"))
            refuel_car = car.fuel(refuel)
            print("Added {} units of fuel".format(refuel_car))
        else:
            print("Invalid Choice")
            print()
            print(car)
            print(MENU)
    print("\nGood bye {} driver".format(name))
main()