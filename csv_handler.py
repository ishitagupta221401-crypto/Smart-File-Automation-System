import csv

def read_csv(filename):

    try:
        with open(filename, "r") as file:

            reader = csv.reader(file)

            print("\ncsv Data:\n")

            for row in reader:
                print(row)

    except FileNotFoundError:
        print("CSV file not found.")
