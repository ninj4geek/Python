import random
import csv


def get_burn_center():
    with open('/home/patrick/Downloads/burn_centers.csv') as csv_file:
        reader = csv.reader(csv_file)
        rownum = random.randrange(0, 159, 1)
        rows = list(reader)
        print(''.join(rows[0])) #rownum goes where 0 is


def handle_command(command):
    command = command.lower()

    if command == "!getalistofburncenters":
        print("Ouch. Here's a burn center for you to contact: \n")
        get_burn_center()


if __name__ == '__main__':
    handle_command(input("Enter command: "))
