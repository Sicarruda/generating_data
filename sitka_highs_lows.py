from pathlib import Path
from datetime import datetime

import csv
import matplotlib.pyplot as plt


# path = Path("generating_data/weather_data/sitka_weather_2021_simple.csv")
path= Path("generating_data/weather_data/death_valley_2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)


# Print the index of the header
# for index, column_header in enumerate(header_row):
# print(index, column_header)

# Extract dates, high and low temperatures.
highs, dates, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        hight = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")

    else:
        dates.append(current_date)
        highs.append(hight)
        lows.append(low)

# Plot the high temperatures.
plt.style.use("bmh")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Format plot.
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel("", fontsize=20)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
