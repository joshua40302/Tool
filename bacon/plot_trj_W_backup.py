# This script is used to read the dump file from LAMMPS 
# and plot the trajectories of individual helium depth

import pandas as pd
import numpy as np


def read_dump(path, frame_num: int):
    filename = path + 'W.' + str(frame_num) + '.coord'
    df = pd.read_csv(filename, sep="\s+", header=None, skiprows=9, \
                      names=["ID","type","x","y","z"])
    #df = df.drop(columns="type")
    
    df = df.sort_values(by='ID', ascending=True)
    df = df.to_numpy()
    return df


#part = 48
frame_s = 0    # start frame
frame_e = 400     # end frame
frame_i = 1       # frame interval
tot_atom = 4007   # total atom numbers
n_W = 2
dt = 0.00001

n_frame = int((frame_e - frame_s )/frame_i)
df1 = pd.DataFrame(['4007'])
count = 1

df = pd.read_csv('pre.atom', sep="\s+", header=None, \
                 names=["ID","type","x","y","z"])
W_ID = []


      
###### Find mobilized W and store ID ######################
row_s = 4016*0
row_e = 4016*1
temp_df1 = df.iloc[row_s:row_e,0:5]
temp_df1 = temp_df1.iloc[9:4016,0:5].apply(pd.to_numeric)
temp_df1 = temp_df1.sort_values(by=["ID"], ascending=True)
row_s = 4016*250
row_e = 4016*251
temp_df2 = df.iloc[row_s:row_e,0:5]
temp_df2 = temp_df2.iloc[9:4016,0:5].apply(pd.to_numeric)
temp_df2 = temp_df2.sort_values(by=["ID"], ascending=True)
count = 0
for i in range(0,4000):
    if abs(temp_df1.iloc[i,4]-temp_df2.iloc[i,4]>2.0):
        W_ID.append(temp_df1.iloc[i,0])
        count=count+1
############################################################

del temp_df1, temp_df2

# Initialize W trajectory dataframe
trj_W = pd.DataFrame(0, index=np.arange(0, count), columns=np.arange(1))
time = pd.DataFrame(0, index=np.arange(1), columns=np.arange(0, n_frame))


for i in range(frame_s,frame_e,frame_i):
    row_s = 4016*i
    row_e = 4016*(i+1)
    temp_df = df.iloc[row_s:row_e,0:5]

    timestep = pd.to_numeric(temp_df.iloc[1,0])     # read timestep
    temp_df = temp_df.iloc[9:4016,0:5].apply(pd.to_numeric)
    
    count = 0
    for t in W_ID:
    #temp_df = temp_df.sort_values(by=["ID"], ascending=True)
        temp_z = temp_df[temp_df["ID"] == W_ID[count]]
        temp_z = temp_z.iloc[0,4]
        trj_W.loc[count,i] = temp_z
        count = count + 1
        
    temp_df = temp_df.sort_values(by=["z"], ascending=True)
    temp_df = temp_df.iloc[0:tot_atom,0:5].apply(pd.to_numeric)
    
    z_pos1 = temp_df.iloc[0,4]    # z postion of first atom (1st smallest)
    z_pos2 = temp_df.iloc[1,4]    # z postion of first atom (2nd smallest)
    z_pos3 = temp_df.iloc[2,4]    # z postion of first atom (3rd smallest)
    
    
    ###### Calculate the surface height and check adatoms ###########
    if abs(z_pos1-z_pos3) > 0.5:        # check number 1 adatom
        if abs(z_pos2-z_pos3) > 0.5:    # check number 2 adatom
            surf_h = temp_df.iloc[2:103,4].mean() # 100 atoms at surface, 2 adatoms
            #print(surf_h)
        else:
            surf_h = temp_df.iloc[1:102,4].mean() # 100 atoms at surface, 1 adatoms
            #print(surf_h)
    else:
        surf_h = temp_df.iloc[0:101,4].mean() # 100 atoms at surface, no adatoms
        #print(surf_h)
    #################################################################
    
    if i==0:
        trj_W.loc[:,0] = trj_W.loc[:,0] - surf_h
        time.loc[0,0]  = timestep * dt
    else:
        trj_W.loc[:,i] = trj_W.loc[:,i] - surf_h
        #trj_W.loc[1,i] = b.iloc[0,4] - surf_h
        time.loc[0,i]  = timestep * dt
    

        
fig = plt.figure()
plt.plot(time.iloc[0,:],trj_W.iloc[0,:])
plt.plot(time.iloc[0,:],trj_W.iloc[1,:])
plt.plot(time.iloc[0,:],trj_W.iloc[2,:])
plt.plot(time.iloc[0,:],trj_W.iloc[3,:])
plt.plot(time.iloc[0,:],trj_W.iloc[4,:])
plt.plot(time.iloc[0,:],trj_W.iloc[5,:])
plt.plot(time.iloc[0,:],trj_W.iloc[6,:])
plt.plot(time.iloc[0,:],trj_W.iloc[7,:])
plt.plot(time.iloc[0,:],trj_W.iloc[8,:])
plt.title("Tungsten depth")
plt.xlabel("t (ps)")
plt.ylabel(r"individual W atom depth ($\AA$)")
plt.ylim([-2,7])
plt.savefig("trj_W",dpi=300, bbox_inches='tight')

test = []
PotEng = pd.read_csv('PotEng.log')
for i in range(40):
    test.append(PotEng.iloc[10*i:10*(i+1),0].min())
fig2 = plt.figure()
test = test - PotEng.iloc[-1,0]
plt.plot(time.iloc[0,::10],test)
plt.title("Energy evolution")
plt.xlabel("t (ps)")
plt.ylabel("E (eV)")
plt.savefig("PotEng",dpi=300, bbox_inches='tight')
