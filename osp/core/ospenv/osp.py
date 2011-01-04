#! /usr/bin/python
#
# osp.py
#
# Module to contain central stuff used in all the osp* scripts.
#

import os

# Globals
envars = [ 'OSP_JOB',
           'OSP_JOB_CODE',
           'OSP_JOB_NAME',
           'OSP_SEQ',
           'OSP_SEQ_NAME',
           'OSP_SHOT',
           'OSP_SHOT_NAME', ]

job_folder_name = 'jobs'
job_osp_folder_name = '_osp'
job_config_file_name = 'osp_show_config.py'

osp_vols = os.getenv('OSP_VOLS')


##
## Methods
##

def volumes():
    """Return a list of all OSP-enableled volumes available on this machine."""
    
    return [vol for vol in osp_vols.split(':') if os.path.exists(vol)]

def job_dirs():
    """Return a list of the paths to all jobs folders on all the OSP-enableled volumes available on this machine."""
    
    dirs = [os.path.join(vol, job_folder_name) for vol in volumes()]
    return [dir for dir in dirs if os.path.exists(dir)]    
    

def jobs():
    """Return a list of the paths to all OSP-enableled jobs available on this machine."""
    
    joblist = []
    for jobd in job_dirs():
        joblist += [os.path.join(jobd, d) for d in os.listdir(jobd)]
    return [job for job in joblist if os.path.exists(job_config_file(job))]
        
    
def job_config_file(job_path):
    """Accept the path to a job's root directory and return the path to that job's config file (whether or not it exists.)"""
    
    return os.path.join(job_path, job_osp_folder_name, job_config_file_name)

if __name__ == "__main__":
    pass
