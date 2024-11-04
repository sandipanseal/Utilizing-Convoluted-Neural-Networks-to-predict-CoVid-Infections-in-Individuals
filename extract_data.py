import os
import sys
import subprocess
import numpy as np
import glob
import json
import pandas as pd

'''
This script creates a folder "covid_Extracted_data" inside which it extracts all the wav files in the directories date-wise
'''

covid_data_dir = os.path.abspath('.') # Local Path of covid_data Repo
covid_extracted_data_dir = os.path.join(covid_data_dir, 'covid_Extracted_data')  

if not os.path.exists(covid_data_dir):
    raise("Check the Covid dataset directory!")

if not os.path.exists(covid_extracted_data_dir):
    os.makedirs(covid_extracted_data_dir) # Creates the covid_extracted_data folder if it doesn't exist

dirs_extracted = set(map(os.path.basename,glob.glob('{}/202*'.format(covid_extracted_data_dir))))
dirs_all = set(map(os.path.basename,glob.glob('{}/202*'.format(covid_data_dir))))

dirs_to_extract = list(set(dirs_all) - dirs_extracted)

for d in dirs_to_extract:
    p = subprocess.Popen('cat {}/{}/*.tar.gz.* |tar -xvz -C {}/'.format(covid_data_dir, d, covid_extracted_data_dir), shell=True)
    p.wait()


print("Extraction process complete!")
