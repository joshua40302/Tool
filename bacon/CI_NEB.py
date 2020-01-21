# This script is used to read the NEB log file from LAMMPS 
# and generate PotEng vs reaction coordinate and calculate
# Ea, i.e. energy barrier
# Author: Josh Chen
# Date: May/16/2019

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

step = 25


df = pd.read_csv('CI_NEB.log', sep="\s+", skiprows=3, header=None)  
PotEng_last = df.iloc[step,104]
temp = df.iloc[step,10:105:2] 
PotEng = pd.to_numeric(temp)
#PotEng = PotEng - PotEng_last

#PotEng = PotEng - PotEng_last
Coord  = pd.to_numeric(df.iloc[step,9:104:2])
PotEng = PotEng.tolist()
Coord = Coord.tolist()
fig = plt.figure(figsize=[4.8,4])
ax = fig.add_subplot(1, 1, 1)


plt.scatter(Coord, PotEng,s=40,facecolors='none', edgecolors='#1f77b4',\
            linewidth=0.8)
xtick_major = np.linspace(0, 1, num=6)
ytick_major = np.linspace(0, 12, num=7)
xtick_minor = np.linspace(0, 1, num=11)
ytick_minor = np.linspace(0, 12, num=13)
ax.set_xticks(xtick_major)
ax.set_yticks(ytick_major)
ax.set_xticks(xtick_minor, minor=True)
ax.set_yticks(ytick_minor, minor=True)

#ax.tick_params(which='major', length=5, color='k')
#plt.minorticks_on()

plt.xlabel("Normalized reaction coordinate")
plt.ylabel("E (eV)")
plt.title("CI-NEB")

print(max(PotEng)-PotEng[0])


plt.savefig("fig_NEB",dpi=300, bbox_inches='tight')