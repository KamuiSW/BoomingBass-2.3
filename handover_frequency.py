import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_low = pd.read_excel("Data/low_amplitude_response.xlsx")
file_medium = pd.read_excel("Data/medium_amplitude_response.xlsx")
file_high = pd.read_excel("Data/high_amplitude_response.xlsx")

plt.plot(file_low["Frequency (Hz)"], file_low["Power Response [dB]"], label="Low", color="blue")
plt.plot(file_medium["Frequency (Hz)"], file_medium["Power Response [dB]"], label="Medium", color="green")
plt.plot(file_high["Frequency (Hz)"], file_high["Power Response [dB]"], label="High", color="red")

plt.xlabel("Frequency (Hz)")
plt.ylabel("Power Response [dB]")

plt.xscale('log',base=10)

plt.grid(True, alpha=0.3)

def intersections(first, second, f_min, f_max):
    freq = "Frequency (Hz)"
    db = "Power Response [dB]"

    first = first.sort_values(freq)
    second = second.sort_values(freq)

    start = max(f_min, first[freq].min(), second[freq].min())
    end = min(f_max, first[freq].max(), second[freq].max())
    if start > end:
        return []

    f = np.unique(np.r_[first[freq], second[freq], start, end])
    f = f[(f >= start) & (f <= end)]

    # Interpolate in log-frequency to match your plot.
    x = np.log10(f)
    y1 = np.interp(x, np.log10(first[freq]), first[db])
    y2 = np.interp(x, np.log10(second[freq]), second[db])
    difference = y1 - y2

    points = []
    for i, diff in enumerate(difference):
        if diff == 0:
            points.append((float(f[i]), float(y1[i])))
        elif i + 1 < len(f) and diff * difference[i + 1] < 0:
            fraction = diff / (diff - difference[i + 1])
            crossing_x = x[i] + fraction * (x[i + 1] - x[i])
            crossing_db = y1[i] + fraction * (y1[i + 1] - y1[i])
            points.append((float(10**crossing_x), float(crossing_db)))

    return points


low_medium = intersections(file_low, file_medium, 48, 58)
medium_high = intersections(file_medium, file_high, 750, 800)

print("Low to medium:", low_medium)
print("Medium to high:", medium_high)

plt.show()

