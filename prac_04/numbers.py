def main():
    numbers = []
    for i in range(5):
        i = int(input("Please enter a number: "))
        numbers.append(i)
    print("The first number is", numbers[0])
    print("The last number is", numbers[-1])
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))
    print("The average of the numbers is", sum(numbers) / 5)


main()
