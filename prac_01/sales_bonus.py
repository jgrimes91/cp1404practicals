"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))

while sales > 0:
    if sales < 1000:
        print("You get $", sales * .1, " bonus")
    elif sales >= 1000:
        print("You get $", sales * .15, " bonus")
    sales = float(input("Enter sales: $"))