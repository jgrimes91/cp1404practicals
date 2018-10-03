from prac_08.taxi import Taxi


def main():
    prius = Taxi("Prius", 100)
    prius.drive(40)
    print(prius)

    prius.start_fare()
    prius.drive(100)
    print(prius)


main()
