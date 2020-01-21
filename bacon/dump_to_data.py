# This script is used to read the dump file from LAMMPS 
# and generate coordinate data file for read_data commnads in LAMMPS

bin_step = 10000    # every N step then output one coordinate

dt = 0.00001
step = 1000

bin_step = int(bin_step/step)

data = open("TM.coord", 'r')
a = data.readlines() 
outpt = open("test",'w') 
#print(a[])

for i in range(1,41,1):
    filename = "TM_coord_" + str(i)
    outpt = open(filename,'w') 
    outpt.write("LAMMPS data file via write_data, version 16 Mar 2018\n")
    outpt.write(" \n")
    outpt.write("4007 atoms\n")
    outpt.write("2 atom types\n")
    outpt.write(" \n")
    outpt.write("0.0000000000000000e+000 3.1619999999999997e+001 xlo xhi\n")
    outpt.write("0.0000000000000000e+000 3.1619999999999997e+001 ylo yhi\n")
    outpt.write("0.0000000000000000e+000 9.4859999999999999e+001 zlo zhi\n")
    outpt.write(" \n")
    outpt.write("Masses\n")
    outpt.write(" \n")
    outpt.write("1 183.84\n")
    outpt.write("2 4.0026\n")
    outpt.write(" \n")
    outpt.write("Atoms # atomic\n")
    outpt.write(" \n")
    
    line_start = 4016*i*bin_step + 9
    line_end   = 4016*i*bin_step + 4016
    
    for line in range(line_start,line_end,1):
    #write line to output file
        outpt.write(a[line])
        
    outpt.close()
#outpt.write(cb[0])
# =============================================================================
# part = 48
# 
# df1 = pd.DataFrame(['4007'])
# count = 1
# for i in range(10,part*10+1,10):
#     row_skip = 4007*i + 9*(i+1)
#     df = pd.read_csv('pre.atom', sep="\s+", skiprows=row_skip, header=None, \
#                      nrows=4007)  
#     filename = 'coords.initial.' + str(count)
#     df1.to_csv(filename,index=False, header=None)
#     df.to_csv(filename,float_format='%.6f',sep=' ', columns=[0,2,3,4], \
#               index=False, mode='a', header = None)
#     print(filename) 
#     count = count + 1
#     
# =============================================================================
#a=df.columns
#a = df[4].idxmin()  # Find index of the minimum value
#b = df[4].min()     # Find minimum value
#c = df.sort_values(by=[4]) # Sort ascending of z-axis value
#print(c.iloc[1,4])  
    


