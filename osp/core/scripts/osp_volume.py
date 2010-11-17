#! /usr/bin/python
#
# osp_volume.py
#
# Tim BOWMAN [puffy@netherlogic.com]
#
# Part of the Open Source Pipeline storage volume auto-detection system.
#
# The output from osp_volume.py is executed in osp_volumes.sh in order to set an
# environment variable which locates this volume for this machine. The goal is
# to be able to refer to mounted devices via the same environment variable
# across multiple systems or platforms, even when the devices have different 
# names on different machines.
#
# Put a copy of this script in the root of each disk or volume that OSP needs to
# know about. Don't forget to change the value of volname.
#
# Each volume must have a unique name!
#

import os

# Change the volume name here:
volname = "MY_NAME"

volpath = os.path.dirname(os.path.realpath(__file__))
print 'export OSP_VOL_' + volname + '=' + volpath
print 'export OSP_VOL_NAME=' + volname

if 'OSP_VOLS' in os.environ:
    print 'export OSP_VOLS=$OSP_VOLS:' + volpath
else:
    print 'export OSP_VOLS=' + volpath