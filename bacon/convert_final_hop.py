# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 09:29:39 2019

@author: Josh Chen
"""

import pandas as pd
import numpy as np
import os

input_file = "TM.800000.coord"
otput_file = input_file + ".final"

if __name__ == "__main__":
    df = pd.read_csv(input_file, sep="\s+", header=None, skiprows=9, \
                     names=["ID","type","x","y","z"])
    
    df = df.drop(columns=["type"])
    
    atom_num = df.index[-1] + 1       # index of last row + 1 
    
    # check final coord file exist ###
    if os.path.exists(otput_file):
        os.remove(otput_file)
        print("Remove %s file" % (otput_file))
    ##################################

    f = open(otput_file, 'a')
    f.write(str(atom_num)+'\n')
    df.to_csv(f, header=False, index=False, sep=' ',  float_format='%.15f')
    f.close()
    print("File convert successfully!")