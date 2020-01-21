# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 12:55:41 2019

@author: Josh Chen
"""

import pandas as pd 
import numpy as np
import os

def read_dump(path, frame_num: int):
    #state: read different type of data
    filename = path + 'minimize.' + str(frame_num) + '.coord'
    df = pd.read_csv(filename, sep="\s+", header=None,  \
                      names=["ID","type","x","y","z"])
    timestep = df.iloc[1,0]
    box_xlo, box_xhi  = df.iloc[5,0], df.iloc[5,1]
    box_ylo, box_yhi  = df.iloc[6,0], df.iloc[6,1]
    box_zlo, box_zhi  = df.iloc[7,0], df.iloc[7,1]
    box = [[box_xlo, box_xhi], [box_ylo, box_yhi], [box_zlo, box_zhi]]
    box = pd.DataFrame(box, columns=['lo', 'hi'])
    return df, box

def gen_init_hop(data, path, atom_num, box_dim):
    if(os.path.isfile(path)):
        os.remove(path)
        f = open(path, 'a')
        print('blank init.hop created successfully!')
    else:
        f = open(path, 'a')
        print('blank init.hop created successfully!')
    
    f.write("LAMMPS data file via write_data, version 16 Mar 2018\n")
    f.write(" \n")
    f.write(str(atom_num) + ' atoms\n')
    f.write("2 atom types\n")
    f.write(" \n")
    f.write(str(box_dim.iloc[0,0]) + "  " + str(box_dim.iloc[0,1]) + "  xlo xhi\n")
    f.write(str(box_dim.iloc[1,0]) + "  " + str(box_dim.iloc[1,1]) + "  ylo yhi\n")
    f.write(str(box_dim.iloc[2,0]) + "  " + str(box_dim.iloc[2,1]) + "  zlo zhi\n")
    f.write(" \n")
    f.write("Masses\n")
    f.write(" \n")
    f.write("1 183.84\n")
    f.write("2 4.0026\n")
    f.write(" \n")
    f.write("Atoms # atomic\n")
    f.write(" \n")
    
    data = data.tail(n=atom_num)
    data = data.apply(pd.to_numeric)
    data.to_csv(f, float_format="%.15f", header=None, sep=' ', index=False, line_terminator='\n')

def gen_finl_hop(min_path, finl_path, atom_num, frame_num: int):
    if(os.path.isfile(finl_path)):
        os.remove(finl_path)
        f = open(finl_path, 'a')
        print('blank init.hop created successfully!')
    else:
        f = open(finl_path, 'a')
        print('blank init.hop created successfully!')
    filename = min_path + 'minimize.' + str(frame_num) + '.coord'
    data = pd.read_csv(filename, sep="\s+", header=None,  \
                      names=["ID","type","x","y","z"])

    f.write(str(atom_num) + '\n')
    data = data.tail(n=atom_num)
    data = data.apply(pd.to_numeric)
    data = data.sort_values(by=['ID'])
    data = data.drop(['type'], axis=1)
    data.to_csv(f, float_format="%.15f", header=None, sep=' ', index=False, line_terminator='\n')
    
'''    

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
'''