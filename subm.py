#Cylindrical_pit submit file
import os
import numpy as np

workingdir=os.getcwd()
 
#k1=['0.4','0.5','0.6','0.7','0.8','0.9','1.0','1.1','1.2']
#r_b=['1.0','1.1','1.2','1.3','1.4','1.5','1.6','1.7','1.8','1.9','2.0']
k1  = 0.01*np.arange(35, 41, 1)
k1  = np.around(k1, decimals=2)
k1  = list(map(str,k1))
r_b  = np.arange(40.0,52.0, 2)
r_b  = np.round_(r_b,1)
r_b  = list(map(str,r_b))

a=0
b=0

for k1i in range(a,len(k1)):
    for r_bi in range(b,len(r_b)):
        os.chdir(workingdir+'/'+k1[k1i]+'/'+r_b[r_bi])
        #os.system('cp '+workingdir+'/smes.6.1.0/proposalfig.m ./')
        #os.system('cp '+workingdir+'/smes.6.1.0/proposalfig1.m ./')
        os.system('bsub < lsf.runfile')
        print("Job:"+k1[k1i]+"_"+r_b[r_bi]+"submitted")
        b = b + 1
        if  b == len(r_b):
            #b = a + 1
            b = 0
    a = a + 1

