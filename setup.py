#Cylintrical_pits setup file
import os
import numpy as np

workingdir=os.getcwd()
#print(workingdir)
#k1=['0.3', '0.6', '0.9', '1.2']
#k2=['0.3', '0.6', '0.9', '1.2']
#k1 = np.linspace(0.5,1.5,11)
#k1 = str(list(np.rint(k1)))
#k1=['0.4','0.5','0.6','0.7','0.8','0.9','1.0','1.1','1.2']
k1  = 0.01*np.arange(44.0, 45.0, 1)
k1  = np.around(k1, decimals=2)
k1  = list(map(str,k1))
r_b  = 0.01*np.arange(10.0,36.0, 1)
r_b  = np.around(r_b,decimals=2)
r_b  = list(map(str,r_b))
#r_b=['1.0','1.1','1.2','1.3','1.4','1.5','1.6','1.7','1.8','1.9','2.0']

#phasey=['0.5', '1.0', '3.0', '6.0', '9.0', '12.0','16.0','20.0']
#h=['0.09', '0.05', '0.01', '0.005', '0.001', '0.0005']
#phasex=['0.5', '1.0','3.0']
#phasey=['0.5', '1.0','3.0']
#lx    =['0.3', '0.7','2.5']
#ly    =['0.3', '0.7','2.5']

#Consider the repeat of same cases
a=0
b=0

for k1i in range(a,len(k1)):
    #os.system('mkdir '+workingdir+'/'+k1[k1i])
    for r_bi in range(b,len(r_b)):
        #os.system('mkdir '+workingdir+'/length/'+k1[k1i]+'/'+r_b[r_bi])
        os.chdir(workingdir+'/k/lx37_ly16/'+k1[k1i]+'/'+r_b[r_bi])
        #os.system('cp -r '+workingdir+'/smes.8.3.0/esxy_data ./')
        #os.system('cp -r '+workingdir+'/smes.8.3.0/stxy_data ./')
        #os.system('cp -r '+workingdir+'/smes.8.3.0/xyh_data ./')
        os.system('cp -r '+workingdir+'/smes.8.3.0/matlab\ files\ for\ figures ./')
        #os.system('cp '+workingdir+'/smes.8.1.0/analysis.m ./')
        #os.system('cp '+workingdir+'/smes.8.3.0/input.dat ./')
        #os.system('cp '+workingdir+'/smes.8.3.0/lsf.runfile ./')
        #os.system("sed -i '6d' input.dat")
        #os.system("sed -i '5a  phasex=     "+r_b[r_bi]+"' input.dat")
        #os.system("sed -i '7d' input.dat")
        #os.system("sed -i '6a  k2=         "+k1[k1i]+"' input.dat")
        #os.system("sed -i '2d' lsf.runfile")
        #os.system("sed -i '1a #BSUB -J "+k1[k1i]+"_"+r_b[r_bi]+"' lsf.runfile")
        print("ellpise_"+k1[k1i]+"_"+r_b[r_bi])
        b = b + 1
        if  b == len(r_b):
            #b = a + 1
            b = 0
    a = a + 1
        
