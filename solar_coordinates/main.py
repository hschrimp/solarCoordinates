import csv


def main():
    filename = 'planets.csv'
    with open(filename, 'r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            print(row)



if __name__ == "__main__":
    # execute only if run as a script
    main()