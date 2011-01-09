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

# Set paths
export PATH=$PATH:$OSP_HOME/local/ospenv:$OSP_HOME/core/ospenv
export PYTHONPATH=$PYTHONPATH:$OSP_HOME/local/ospenv:$OSP_HOME/core/ospenv
export NUKE_PATH=$NUKE_PATH:$OSP_HOME/local/nuke:$OSP_HOME/core/nuke

alias oenv="set|grep ^OSP"

# Set aliases for ospenv tools
alias ospunset=`ospunset`
alias ospreload=". $OSP_HOME/core/ospenv/osp_env.sh"
function ospjob() { $OSP_HOME/core/ospenv/ospjob "$@" ;}

# Source the local studio environment if it exists.
if [ -e $OSP_HOME/local/scripts/osp_local_env.sh ]
then 
    . $OSP_HOME/local/scripts/osp_local_env.sh
fi

