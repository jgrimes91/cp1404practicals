from prac_08.guitars import Guitar


def main():
    print("Guitar Reader!")

    guitars = []

    in_line = open('guitars.csv', 'r')
    in_line.readlines()

    for line in in_line:
        parts = line.strip().split(',')




main()