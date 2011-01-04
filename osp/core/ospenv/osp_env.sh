#! /bin/bash
#
# Set up the default OSP enviroment. A nifty part of Open Source Pipeline.

echo "Loading OSP core environment."

#export OSP_VERBOSE=True

# Stop if OSP_HOME is not set.
if [ -z "${OSP_HOME}" ]
then 
    echo "OSP_HOME not set. Cannot find OSP scripts."
    exit 1
fi

# Find OSP volumes
unset OSP_VOLS
. $OSP_HOME/core/ospenv/osp_volumes.sh

# Setup paths
export PATH=$PATH:$OSP_HOME/local/scripts:$OSP_HOME/core/scripts
export PYTHONPATH=$PYTHONPATH:$OSP_HOME/local/scripts:$OSP_HOME/core/scripts
export NUKE_PATH=$NUKE_PATH:$OSP_HOME/local/nuke:$OSP_HOME/core/nuke

alias oenv="set|grep ^OSP"
alias ospreload=". $OSP_HOME/core/ospenv/osp_env.sh"

# Source the local studio environment if it exists.
if [ -e $OSP_HOME/local/scripts/osp_local_env.sh ]
then 
    . $OSP_HOME/local/scripts/osp_local_env.sh
fi

