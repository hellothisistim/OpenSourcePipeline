#! /bin/bash
#
# osp_volumes.sh
#
# Tim BOWMAN [puffy@netherlogic.com]
#
# Part of the Open Source Pipeline storage volume auto-detection system.
#
# Sets environment variable shortcuts to each OSP-aware disk or volume by
# looking for and executing a Python script called osp_volume.py in the root of
# each mounted volume. The Python script returns the BASH "export" command which
# sets the shortcut to the volume. The goal is to be able to refer to discs via
# the same environment variable across multiple systems or platforms.
#

# Should probably check OSP_MODE to see if we should be chatty like this or not.
# It might get annoying to the user.
echo -n "OSP volumes:"

# Find mount points
# Linux first
if [ -e /mnt ]
then 
    m=/mnt
fi
# Then OSX
if [ -e /Volumes ]
then 
    m=/Volumes
fi

# Run osp_volume.py if it exists
OSP_VOL_NAME=""
for d in $( ls $m ); do
    if [ -e $m/$d/osp_volume.py ]
    then
        `python $m/$d/osp_volume.py`
        echo -n " "$OSP_VOL_NAME
    fi
done
unset OSP_VOL_NAME

# Clean up
unset m
unset d
echo

