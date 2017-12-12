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
    #do something cool
    print('Hello data in the path'+basedir)
def main(): 
    #load in all the global cariables prepro needs right now this is jsut the path to the data
    basedir='/Users/RachelGreene/fmri_workshop/'
    prepro(basedir) #call prepro to do cool things