# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:05:14 2019

@author: Josh Chen
"""

# Bacon is the tool for LAMMPS data post-processing
# Developed by Josh Chen

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

import plot_trj_He as plt_He
import plot_trj_W  as plt_W
import min_fetch_plt as mfp


trj_path = '../dump/'
minimize_path = '../minimization/dump32_min/'
Pot_path = '../minimization/PotEng2.log'
Figsave_path = '../figure/'
fig_he_name = 'he_trj.png'
fig_w_name = 'W_trj.png'
fig_Pot_name = 'PotEng2.png'
init_hop_path = '../NEB/init.hop'
finl_hop_path = '../NEB/final.hop'
init_config = 100000
finl_config = 600000
dt = 0.00001
timestep = 1000
atom_num = 6148
frame_s = 0    # start frame
frame_e = 400000     # end frame
frame_i = 1000       # frame interval

######################### Switch ##########################
switch = {'he_plot': 1, 'min': 0, 'Poteng': 0, 'w_plot': 0}

############################################################

if __name__ == "__main__":
    ################  Plot Helium trjectory ################
    if(switch['he_plot']==1):
        H0_z = []
        H1_z = []
        H2_z = []
        H3_z = []
        time = []
    
        #frame_s = 0    # start frame
        #frame_e =3000000     # end frame
        #frame_i = 1000       # frame interval
        
        for i in range(frame_s,frame_e,frame_i):
            data = plt_He.read_dump(trj_path,0,i)
            surf_h = plt_He.read_dump(trj_path,1,i)
            H0_z.append(surf_h-data[0,1])
            H1_z.append(surf_h-data[1,1])
            H2_z.append(surf_h-data[2,1])
            H3_z.append(surf_h-data[3,1])
            time.append(i*dt)
    
        fig = plt.figure()
        plt.plot(time,H0_z, time,H1_z, time,H2_z, time,H3_z)
        plt.title("Helium depth")
        plt.xlabel("t (ps)")
        plt.ylabel(r"individual He atom depth ($\AA$)")
        plt.savefig(Figsave_path+fig_he_name,dpi=300, bbox_inches='tight')  
        print("Helium Trjectory Plotted Successfully!")
    
    ################  Find mobilized W and plot ################
    if(switch['w_plot']==1):
        W0_z = []
        W1_z = []
        W2_z = []
        W3_z = []
        time = []
        data_W_i, data_W_e = plt_W.read_dump(trj_path, frame_i, frame_e)
        W_id, num_mobile_W = plt_W.find_mobile_W(data_W_i, data_W_e, atom_num)
        #data_W, surf_h= plt_W.read_trj(trj_path,1000)
        for i in range(frame_s,frame_e,frame_i):
            data_W, surf_h= plt_W.read_trj(trj_path,i)
            #data_W.loc[data_W['ID']==1]
            temp = data_W[data_W['ID']==W_id[0]]
            temp = temp['x'].item()
            W0_z.append(surf_h-temp)
            temp = data_W[data_W['ID']==W_id[1]]
            temp = temp['x'].item()
            W1_z.append(surf_h-temp)
            temp = data_W[data_W['ID']==W_id[2]]
            temp = temp['x'].item()
            W2_z.append(surf_h-temp)
            temp = data_W[data_W['ID']==W_id[3]]
            temp = temp['x'].item()
            W3_z.append(surf_h-temp)
            time.append(i*dt)

        fig = plt.figure()
        plt.plot(time,W0_z, time,W1_z, time,W2_z, time,W3_z)
        #plt.plot(time,W0_z)
        plt.title("Tungsten depth")
        plt.xlabel("t (ps)")
        plt.ylabel(r"individual He atom depth ($\AA$)")
        plt.savefig(Figsave_path+fig_w_name,dpi=300, bbox_inches='tight')  
        print("Helium Trjectory Plotted Successfully!")

    ################  Minimization fetch & plot ################
    if(switch['min']==1):
        data_min, box = mfp.read_dump(minimize_path,init_config)
        data_min = data_min.drop(data_min.index[0:9], axis=0)    #drop first 9 rows
        #data_min = data_min.tail(n=atom_num)
        mfp.gen_init_hop(data_min, init_hop_path, atom_num, box)
        mfp.gen_finl_hop(minimize_path, finl_hop_path, atom_num, finl_config)
#        surf_h = plt_He.read_dump(trj_path,1,i)
#        H0_z.append(surf_h-data[0,1])
#        H1_z.append(surf_h-data[1,1])
#        H2_z.append(surf_h-data[2,1])
#        H3_z.append(surf_h-data[3,1])
#        time.append(i*dt)
  
    ################  Potential energy plot ################
    if(switch['Poteng']==1):
        col=['PotEng'] 
        data_Pot = pd.read_csv(Pot_path, names=col, header=None)
        Pot_time = pd.Series(data_Pot.index) * dt * timestep
        fig_Pot  = plt.figure()
        final_Pot = data_Pot.iloc[670]
        plt.plot(Pot_time[0:1000:30], data_Pot[0:1000:30] - final_Pot)
        plt.title('Potential Energy')
        plt.xlabel("t (ps)")
        plt.ylabel("E (eV)")
        plt.savefig(Figsave_path+fig_Pot_name,dpi=300, bbox_inches='tight')  
        print("Potential Energy Plotted Successfully!")
    
