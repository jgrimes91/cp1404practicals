from prac_08.Car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 100, 4)]

    total_bill = 0

    print("Let's drive!")

    print(MENU)

    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            chosen_taxi = taxis[taxi_choice]
        elif choice == "d":
            chosen_taxi.start_fare()
            distance_to_drive = float(input("Drive how far?"))
            chosen_taxi.drive(distance_to_drive)
            trip_fare = chosen_taxi.get_fare()
            print("Your {} cost you {:2f}".format(chosen_taxi.name, trip_fare))

            total_bill += trip_fare
        else:
            print("Invalid option")
        print("Bill to date: $ {:.2f}".format(total_bill))
        print(MENU)
        choice = input(">>> ").lower()

    print("Total bill cost ${:.2f}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)




def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
