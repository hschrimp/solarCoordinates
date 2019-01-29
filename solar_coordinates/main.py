import csv
from solar_coordinates.ecliptic import Ecliptic

def main():
    e = Ecliptic()
    filename = 'planets.csv'
    with open(filename, 'r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            print(row)
            e.draw_planet(**row)
        e.draw_sun()
        e.wait()





if __name__ == "__main__":
    # execute only if run as a script
    main()