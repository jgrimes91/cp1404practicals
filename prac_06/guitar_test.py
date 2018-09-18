from prac_06.guitar import Guitar

CURRENT_YEAR = 2018

def main():
    """Test for Guitar class"""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    print("My guitar: {}, first made in {}.".format(name, year))

    guitar = Guitar(name, year, cost)
    other_guitar = Guitar("Another Guitar", 2012, 1512.90)

    print("{} get_age() - Expected {}. Got {}.".format(guitar.guitar_name, 96, guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}.".format(other_guitar.guitar_name, 6, guitar.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.guitar_name, True, guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}.".format(other_guitar.guitar_name, False, guitar.is_vintage()))

main()
