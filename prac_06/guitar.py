CURRENT_YEAR = 2018
VINTAGE_AGE = 50


class Guitar:
    def __init__(self, guitar_name="", year=0, cost=0):
        self.guitar_name = guitar_name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : {}".format(self.guitar_name, self.year, self.cost)

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE