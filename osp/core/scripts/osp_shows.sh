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

if [ ${#1} != 0 ]; then
    export OSP_SHOW_CODE=$1
fi

for p in $( echo $OSP_VOLS|tr : " " ); do
    #echo "OSP looking for show root in: "$p
    if [ -e $p/show ]
    then 
        for s in $( ls $p/show ); do
            #echo "Found show: "$s
            if [ -e $p/show/$s/_osp/osp_show.py ]
            then
                `python $p/show/$s/_osp/osp_show.py`
                #echo -n " "$OSP_SHOW_NAME
            fi
        done
    fi
done

if [ -z "${OSP_SHOW}" ]; then
    #echo Show: $OSP_SHOW
    unset OSP_SHOW_CODE
fi

echo __
echo "OSP envars:"
set|grep ^OSP