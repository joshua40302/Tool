import pandas as pd 
df = pd.read_csv('log.lammps', sep="\s+", skiprows=3, header=None)  
print(df) 
D = df
#a = df[4].idxmin()  # Find index of the minimum value
#b = df[4].min()     # Find minimum value
#c = df.sort_values(by=[4]) # Sort ascending of z-axis value
#print(c.iloc[1,4]) 