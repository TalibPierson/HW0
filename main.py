import csv

from update_locations import update_locations

N = 20

with open("update_locations.csv", 'w') as out:
    writer = csv.writer(out)
    for i in range(0, N + 1):
        print(i)
        data = update_locations(2 ** i, 2 ** (N - i))
        writer.writerow([2 ** i, data])
