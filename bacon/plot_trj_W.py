# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 17:19:12 2019

@author: Josh
"""
import pandas as pd
import numpy as np

def read_dump(path, frame_i: int, frame_e: int):
    file_i = path + 'W.' + str(frame_i) + '.coord'
    file_e = path + 'W.' + str(frame_e) + '.coord'
    df1 = pd.read_csv(file_i, sep="\s+", header=None, skiprows=9, \
                      names=["ID","type","x","y","z"])
    #df = df.drop(columns="type")
    
    df1 = df1.sort_values(by='ID', ascending=True)
    df1 = df1.to_numpy()
    
    df2 = pd.read_csv(file_e, sep="\s+", header=None, skiprows=9, \
                      names=["ID","type","x","y","z"])
    #df = df.drop(columns="type")
    
    df2 = df2.sort_values(by='ID', ascending=True)
    df2 = df2.to_numpy()
    return df1, df2

def find_mobile_W(data_i, data_e, atom_num):
    W_ID = []
    count = 0
    for i in range(0,atom_num-4):
        if abs(data_e[i,2]-data_i[i,2]>2.0):
            W_ID.append(int(data_i[i,0]))
            count=count+1
    return W_ID, count

def read_trj(path, frame_num: int):
    filename = path + "W." + str(frame_num) + '.coord'
    df = pd.read_csv(filename, sep="\s+", header=None, skiprows=9, \
                      names=["ID","type","x","y","z"])
    df = df.drop(columns="type")
    
    data = df.sort_values(by='ID')

    #data = df.reset_index(drop=True)
    surf_h = df.sort_values(by='x', ascending=False)
    surf_h = surf_h.to_numpy()
    # one layer of tungsten contains 260 W
    surf_h = np.mean(surf_h[0:260,1])
    return data, surf_h

#沒有選到對的W ID
        

