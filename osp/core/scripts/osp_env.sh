#! /bin/bash
#
# Set up the default OSP enviroment. A nifty part of Open Source Pipeline.

echo "Loading OSP environment."

# Find OSP volumes
unset OSP_VOLS
. $OSP_HOME/core/scripts/osp_volumes.sh

# Setup paths
export PATH=$PATH:$OSP_HOME/local/scripts:$OSP_HOME/core/scripts
export PYTHONPATH=$PYTHONPATH:$OSP_HOME/core/scripts
export NUKE_PATH=$NUKE_PATH:$OSP_HOME/core/nuke:$OSP_HOME/local/nuke

# Remove old show-specific variables
unset OSP_SHOW
unset OSP_SHOW_DIR
unset OSP_SEQ
unset OSP_SHOT

# Set show variables if requested
if [ ${#1} != 0 ]
then
    echo "Show: "$1
    for p in $( echo $OSP_VOLS|tr : " " ); do
        echo "OSP looking for show root in: "$p
        if [ -e $p/show ]
        then 
            for s in $( ls $p/show ) ]; do
                echo "foundit"
            done
        fi
    done
fi

# Set sequence variable if requested
if [ ${#2} != 0 ]
then
    echo "Seq: "$2
fi

# Set shot variable if requested
if [ ${#3} != 0 ]
then
    echo "Shot: "$3
fi

# Source the local studio environment if it exists.
if [ -e $OSP_HOME/local/scripts/osp_local_env.sh ]
then 
    . $OSP_HOME/local/scripts/osp_local_env.sh
fi