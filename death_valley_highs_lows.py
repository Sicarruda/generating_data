from pathlib import Path
import csv

path= Path("generating_data/weather_data/death_valley_2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row= next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)
    