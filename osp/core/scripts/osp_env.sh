#! /bin/bash
#
# Set up the default OSP enviroment. A nifty part of Open Source Pipeline.

echo "Loading OSP environment."

# Find OSP volumes
unset OSP_VOLS
. $OSP_HOME/core/scripts/osp_volumes.sh

# alias show utility
# Don't need this because osp_env.sh is becoming the show utility.
#alias show=$OSP_HOME/scripts/show.sh

export PATH=$PATH:$OSP_HOME/local/scripts:$OSP_HOME/core/scripts

export PYTHONPATH=$PYTHONPATH:$OSP_HOME/core/scripts
export NUKE_PATH=$NUKE_PATH:$OSP_HOME/core/nuke:$OSP_HOME/local/nuke

# Source the local studio environment if it exists.
if [ -e $OSP_HOME/local/scripts/osp_local_env.sh ]
then 
    . $OSP_HOME/local/scripts/osp_local_env.sh
fi