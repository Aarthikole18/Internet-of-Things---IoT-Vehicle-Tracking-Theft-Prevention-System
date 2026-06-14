import random
import time
import csv
from datetime import datetime

lat = 12.9716
lon = 77.5946

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Time", "Latitude", "Longitude"])

    for i in range(100):

        # simulate movement
        lat += random.uniform(-0.001, 0.001)
        lon += random.uniform(-0.001, 0.001)

        writer.writerow([datetime.now(), lat, lon])

        print("Updated:", lat, lon)

        time.sleep(1)