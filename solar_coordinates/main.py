import csv
from solar_coordinates.hs import HS
from solar_coordinates.ecliptic import Ecliptic


def main():
    choice = input('Is this our Solar System (Y/N): ')
    tilt = 7.25
    prime_meridian = 266
    star_name = 'Sun'
    filename = 'planets.csv'
    if choice == 'N' or choice == 'n':
        tilt = float(input('Stars Tilt: '))
        prime_meridian = float(input('Direction of Prime Meridian: '))
        star_name = input('Name of the star: ')
        filename = input('Planets file: ')
    choice = input('Do you want to display Ecliptic, H-S, or Overlay (E/H/O): ')
    if choice == 'H':
        hs = HS(tilt, prime_meridian, star_name)
        with open(filename, 'r', newline='') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                print(row)
                hs.draw_planet(**row)
            hs.draw_sun()
            hs.wait()
    elif choice == 'E':
        e = Ecliptic()
        with open(filename, 'r', newline='') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                print(row)
                e.draw_planet(**row)
            e.draw_sun()
            e.wait()
    else:
        e = Ecliptic()
        with open(filename, 'r', newline='') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                print(row)
                e.draw_planet(**row)
            e.draw_sun()
        hs = HS(tilt, prime_meridian, star_name)
        with open(filename, 'r', newline='') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                print(row)
                hs.draw_planet(**row)
            hs.draw_sun()
            hs.wait()


if __name__ == "__main__":
    # execute only if run as a script
    main()