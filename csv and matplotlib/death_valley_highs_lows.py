import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, and high and low temperatures
    dates, highs, lows =[], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2],'%Y-%m-%d')
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs,c ='red', alpha = 0.5)
ax.plot(dates, lows, c ='blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

ax.set_title('Daily high and low temperature')
ax.set_xlabel("Dates")
ax.set_ylabel("Temperature (F)")
plt.tick_params(axis='both', which ='major')

plt.show()