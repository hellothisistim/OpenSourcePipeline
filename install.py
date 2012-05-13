#! /usr/bin/python
#
# install
# 
"""
Installs Open Source Pipeline (OSP) on the local computer.

OSP puts it's one "hook" into a computer's configuration via 
Python's site-packages. [http://docs.python.org/library/site.html] 
This script will add or update a path configuration file 
("osp.pth") in the first available site-packages directory on the 
local system, allowing the osp module to be imported in Python.
"""

# From Python
#import datetime
import os.path
#import shutil
#import sys
import site
import logging
from optparse import OptionParser

## -----------------------------------------------------------------------------
## GLOBALS
## -----------------------------------------------------------------------------

#verbose = False
path_config_filename = 'osp.pth'

#Set up logging
log = logging.getLogger(__file__)
log.setLevel(level=logging.DEBUG)

# If we find one, add osp.pth to that directory.

## -----------------------------------------------------------------------------
## METHODS
## -----------------------------------------------------------------------------

def findInstallLocation():
    """Search the list of all the possible locations for site-packages for one that actually exists. Return the first one found.
    """

    pkgs = site.getsitepackages()
    for location in pkgs:
        if os.path.exists(location):
            return location
    # Didn't find one. Better throw an error. 
    # (Is it even possible for this to happen? tb)
    raise Exception("No site-packages directory found on this system. Tried these locations and none exist: %s" % ", ".join(pkgs))

def install(location):
    """Replace any existing osp.pth file in the install location with a new one.
    """
    
    log.debug('Starting installation to %s' % location)
    # Assume this script is in the root of the OSP install.
    osp_dir = os.path.dirname(os.path.abspath(__file__))
    log.debug('OSP home is %s' % osp_dir)
    file_contents = """# Open Source Pipeline\n%s\n""" % osp_dir
    path_config_file = os.path.join(location, path_config_filename)
    log.debug('Writing path configuration file to %s' % path_config_file)
    out = open(path_config_file, 'w')
    out.write(file_contents)
    out.close()
    log.debug('Installation finished.')
    
def remove():
    pass
    
## -----------------------------------------------------------------------------
## MAIN
## -----------------------------------------------------------------------------

if __name__ == '__main__':

    parser = OptionParser(usage = """install [options]
    
    Install Open Source Pipeline (OSP) on this computer. 
    
    Enables OSP by adding a path configuration file ("osp.pth") containing the path to the Open Source Pipeline module.
    """)
    parser.add_option('-v', '--verbose', action = 'store_true', dest = 'verbose', 
                      default = False, help = 'Verbose')
    parser.add_option('-r', '--remove', action = 'store_true', dest = 'remove',  
                      default = False, help = 'Remove OSP configuration')
    
    (options, args) = parser.parse_args()
    
    verbose = options.verbose
    
    if options.remove: uninstall()
    else: install()
