# This script is used to read the dump file from LAMMPS 
# and plot the trajectories of individual helium depth

import pandas as pd 
import numpy as np

def read_dump(path, state: int, frame_num: int):
    #state: read different type of data
    switcher = {        
            0: "He.", 
            1: "W.", 
            2: "TM.", 
    }
    case = switcher.get(state)
    filename = path + case + str(frame_num) + '.coord'
    df = pd.read_csv(filename, sep="\s+", header=None, skiprows=9, \
                      names=["ID","type","x","y","z"])
    df = df.drop(columns="type")
    
    if state == 0:
        df = df.sort_values(by='ID')
        df = df.to_numpy()
        return df
    elif state == 1:
        df = df.sort_values(by='x', ascending=False)
        df = df.to_numpy()
        # one layer of tungsten contains 260 W
        surf_h = np.mean(df[0:260,1])
        return surf_h
        
