#! /usr/bin/python
#
# osp_show.py
#
# The output from osp_show.py is executed in osp_shows.sh in order to set an
# environment variable which locates this show for this machine. The goal is
# to be able to refer to show root directories via the same environment variable
# across multiple systems or platforms, even when the devices have different 
# names on different machines.
#
# Put a copy of this script in the _osp directory and don't forget to change the
# value of showcode!
#
# Each show must have a unique showcode!
#

import os
import sys

# Set show specifics here:
showcode = "SHOWCODE"
showname = "ShowName"

if __name__ == '__main__':
    requested_code = os.getenv('OSP_SHOW_CODE')
    
    # If OSP_SHOW_CODE is not set, echo the show's name and code
    if requested_code is None:
        print 'echo ' + showcode + " : " + showname
        #sys.exit()
    
    # If showcode matches the requested code in sys.argv[1], export the variables
    # for this show.
    elif requested_code == showcode:
        # Find the show root. It's up one directory level.
        thispath = os.path.dirname(os.path.realpath(__file__))
        showpath = os.path.split(thispath)[0]
        
        print 'export OSP_SHOW=' + showpath
        print 'export OSP_SHOW_NAME=' + showname
        print 'export NUKE_PATH=$NUKE_PATH:$OSP_SHOW_DIR'
        