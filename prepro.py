#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:53:57 2017

@author: RachelGreene
"""

import glob
import os
import pdb
import subprocess
import argparse
import datetime
import shutil

def prepro(basedir):
    #do cool stuff here
    print('Hello data in the path'+basedir)
def main(): 
    #load in all the global cariables prepro needs right now this is just the path to the data
    basedir='/Users/RachelGreene/day01_fmriworkshop/'
    prepro(basedir) #call prepro to do cool things
main ()

os.system(bet input output -F)
print(os.system('echo $FSLDIR)) 
    #this doesn't work in spyder but does in jupiter notebook

input=glob.glob('/Users/RachelGreene/fMRI_Analysis_Training_Data_122017/data/sub-*/func/sub-*_task-bart_bold.nii.gz')
len(input)
x=input[1]
print('my path is '+x)
y=x.split('/')
print(y)
whatcomp=y[2]
sub=y[5]
print(sub)

subtask=input[1].split('/')[7].split('.')[0]
#subtast=subtask.strip('nii.gz')
print(subtask)

output=subtask+'_brain'
print(output)

#os.system('bet' x output '-F')
    #this doesn't work in python so use below
os.system ('bet %s %s -F'%(x, output))

input
basedir='/Users/RachelGreene/fMRI_Analysis_Training_Data_122017/data/'
path=os.path.join(basedir,'sub-*','func','sub-*bart*.nii.gz')
print(path)
input=glob.glob(path)
len(input[1:5])

def prepro(basedir):
    for item in glob.glob(os.path.join(basedir,'sub-*','func','sub-*bart*.nii.gz')):
        input=item
        output_path=item.split('.')[0]
        output=output_path+('_brain')
        os.system("bet %s %s -F"%(input, output))
        pdb.set_trace()
def main(): 
    basedir='/Users/RachelGreene/fMRI_Analysis_Training_Data_122017/data/'
    prepro(basedir) 
main()
