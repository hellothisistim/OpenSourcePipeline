import sys
import os
import json


if 'osp.core' in sys.modules:
    reload(core)
else:
    import core


"""
Here's how I'd like stuff to work.


objects:
osp.Environment()
    volumes()  -- osp-enabled volumes
    job()
    sequence()
    shot()
    task()

osp.Volumes()
    load() -- find all osp-enabled volumes on this machine
    
osp.Volume()
    path
    name

osp.Job()
    name - full name
    path
    code - abbreviated name for filesystem
    readConfigFile() -- load configuration from JSON config file

"""

##
## Globals
##


volumes = core.Volumes()

##
## From the alpha v0.001 of OSP:

"""
#! /usr/bin/python
#
# osp.py
#
# Module to contain central stuff used in all the osp* scripts.
#

import os

# Globals
job_envars = { 'OSP_JOB_PATH':'Job Path',
           'OSP_JOB_CODE':'Job Code',
           'OSP_JOB_NAME':'Job Name',
           'OSP_SEQ_PATH':'Sequence Path',
           'OSP_SEQ_NAME':'Sequence Name',
           'OSP_SHOT_PATH':'Shot Path',
           'OSP_SHOT_NAME':'Shot Name', }

job_folder_name = 'jobs'
job_osp_folder_name = '_osp'
job_config_file_name = 'osp_show_config.py'

osp_vols = os.getenv('OSP_VOLS')


##
## Methods
##

def volumes():
    "    Return a list of all OSP-enableled volumes available on this machine."
    
    return [vol for vol in osp_vols.split(':') if os.path.exists(vol)]

def job_dirs():
    "
    Return a list of the paths to all jobs folders on all the OSP-enableled volumes available on this machine.
    "
    
    dirs = [os.path.join(vol, job_folder_name) for vol in volumes()]
    return [dir for dir in dirs if os.path.exists(dir)]    
    

def jobs():
    "
    Return a list of the paths to all OSP-enableled jobs available on this machine.
    "
    
    joblist = []
    for jobd in job_dirs():
        joblist += [os.path.join(jobd, d) for d in os.listdir(jobd)]
    return [job for job in joblist if os.path.exists(job_config_file(job))]
        
    
def job_config_file(job_path):
    "
    Accept the path to a job's root directory and return the path to that job's
    config file (whether or not it exists.)
    "
    
    return os.path.join(job_path, job_osp_folder_name, job_config_file_name)

def job_env(which=None):
    "
    Return a dictionary of environment variable names and their values for all
    job-related OSP evironment variables. If which is provided, filter out the
    variable names that don't conatain the value of which.
    "
    
    out = {}
    for var in job_envars:
        if which and which not in var: continue 
        if os.getenv(var) is not None: out[var] = os.getenv(var)
    return out



if __name__ == "__main__":
    pass
    
    
"""
