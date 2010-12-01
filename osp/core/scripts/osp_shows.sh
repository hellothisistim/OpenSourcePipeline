#! /bin/bash
#
# osp_shows.sh
#
# Tim BOWMAN [puffy@netherlogic.com]
#
# Part of the Open Source Pipeline show detection system.
#
# Usage: osp_shows.sh [show [sequence [shot]]]
#
# Runs through all the show directories in the OSP_VOLS path, executing
# "osp_show.py $OSP_SHOWCODE" in each one in hopes that one of them will match
# the show code and set it's show's envars.
# 
# If run without options, list all available shows along with their respective
# show codes.
#

# Remove old show/seq/shot-specific variables
unset OSP_SHOW
unset OSP_SHOW_NAME
unset OSP_SEQ
unset OSP_SEQ_NAME
unset OSP_SHOT
unset OSP_SHOT_NAME

# Set envars for as many components as were requested.
if [ ${#1} != 0 ]; then
    export OSP_SHOW_CODE=$1
fi

if [ ${#2} != 0 ]; then
    export OSP_SEQ_NAME=$2
fi

if [ ${#3} != 0 ]; then
    export OSP_SHOT_NAME=$3
fi

# Go find all the shows and see if one matches.
for p in $( echo $OSP_VOLS|tr : " " ); do
    if [ -e $p/show ]
    then 
        for s in $( ls $p/show ); do
            if [ -e $p/show/$s/_osp/osp_show.py ]
            then
                `python $p/show/$s/_osp/osp_show.py`
            fi
        done
    fi
done

# If the paths requested above haven't been set, remove the requesting envar.
if [ -z "${OSP_SHOW}" ]; then
    unset OSP_SHOW_CODE
fi

if [ -z "${OSP_SEQ}" ]; then
    unset OSP_SEQ_NAME
fi

if [ -z "${OSP_SHOT}" ]; then
    unset OSP_SHOT_NAME
fi

# Show all the envars that were set. For debugging only.
echo __
echo "OSP envars:"
set|grep ^OSP