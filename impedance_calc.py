import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

bass_abs = pd.read_excel("Data/impedance/Bass_abs_Z.xlsx")
bass_phase = pd.read_excel("Data/impedance/Bass_phase.xlsx")
bass_real_img = pd.read_excel("Data/impedance/Bass_real_imag.xlsx")

med_abs = pd.read_excel("Data/impedance/Mid_abs_Z.xlsx")
med_phase = pd.read_excel("Data/impedance/Mid_phase.xlsx")
med_real_img = pd.read_excel("Data/impedance/Mid_real_imag.xlsx")

High_abs = pd.read_excel("Data/impedance/High_abs_Z.xlsx")
High_phase = pd.read_excel("Data/impedance/High_phase.xlsx")
High_real_img = pd.read_excel("Data/impedance/High_real_imagV2.xlsx")

plt.plot(bass_abs["Frequency (Hz)"], bass_abs["Impedance [Ohm]"], label="Bass", color="blue")
plt.plot(med_abs["Frequency (Hz)"], med_abs["Impedance [Ohm]"], label="Mid", color="green")
plt.plot(High_abs["Frequency (Hz)"], High_abs["Impedance [Ohm]"], label="High", color="red")

i = np.argmin(np.abs(y - target_y))
print(x[i])

impedanceMag_bass = bass_abs["Impedance [Ohm]"]
impedanceMag_med = med_abs["Impedance [Ohm]"]
impedanceMag_High = High_abs["Impedance [Ohm]"]

#if possible, tp finish <3