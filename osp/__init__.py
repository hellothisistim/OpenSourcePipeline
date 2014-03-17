#
# Open Source Pipeline
#
# Tim BOWMAN [puffy@netherlogic.com]
#
"""
With OSP, we're trying not to be tied to a shell or a specific GUI. In 
osp.core we're building objects that we can pass around instead of handing 
around command-line options. 
"""

import datetime
import sys
import os
import json


# if 'osp.core' in sys.modules:
#     reload(core)
# else:
#     import core
if 'osp.env' in sys.modules:
    reload(env)
else:
    import env


## ---------------------------------------------------------------------
## Globals
## ---------------------------------------------------------------------
# Version (major, minor, micro, release level)
version = (0, 0, 1, 'alpha')

ospVolumeTokenName = 'osp-volume.json'  # indicates an OSP-enabled volume.
jobDirName = 'jobs'
jobConfigFileName = 'osp_job_config.json'


## ---------------------------------------------------------------------
## Classes
## ---------------------------------------------------------------------

class BaseShowSection(object):
    """
    All the show sections (Show, Segment, Shot) inherit from this.
    
    """
    
    def __init__(self, path_component, name):
        assert type(path_component) == str
        assert type(name) == unicode
        self._path_component = path_component  # used for the filesystem(s)
        self._name = name  # Full name
        self._osp_version = version
        self._created = datetime.datetime.utcnow()

    def __repr__(self):
        reprString = u"Show: " + self._path_component
        if self.name() is not None:
            reprString += u', ' + self.name()
        return reprString

    def path_component(self):
        return self._path_component
        
    def name(self):
        return self._name
    

class Show(BaseShowSection):
    """Represents a show (a.k.a. job, commercial, project, film, etc.)
    in OSP.

    """

    ## Loading all the sequences in a job isn't so easy -- where do we
    ## load it from? Filesystem? Database?
    #
    # We do'nt load it here. We collect all of that in an Environemnt
    #
    #def _loadSequences(self):
    #    sequences = []
    #    return sequences
       


class Sequence(BaseShowSection):
    """
    Represents a sequence in OSP.
    
    """



class Shot(BaseShowSection):
    """
    Represents a shot in OSP.
    
    """


class Task(BaseShowSection):
    """
    A task is something related to a show, but not to a specific sequence.
    
    """


class Volumes(list):
    """Storage volume auto-detection for OSP-enabled volumes.

    Allows computers which mount filesystems using different
    names to refer to them in a common way. JSON files named
    "osp-volume.json" are placed at the root of attached
    filesystems. The JSON file defines the common name for
    OSP's purposes.

    For example, a Windows box that mounts a networked
    storage as "z:/NAS" and a OSX box that mounts the same
    storage to "/Volumes/NAS" can both refer to them using
    a single name via OSP.
    """

    def __init__(self):
        """Find the OSP-enabled volumes from the volumes mounted on
        this machine."""

        for drive in self._mountedVolumes():
            ospToken = os.path.join(drive, ospVolumeTokenName)
            if os.path.exists(ospToken):
                # Load the JSON
                thisVolume = json.load(file(ospToken))
                self.append(Volume(thisVolume[u'name'], thisVolume[u'path']))

    def reload(self):
        self.__init__()

    def _mountedVolumes(self):
        """Find all mounted drives on this machine."""

        # Known mount points per platform
        # TODO: find correct platform name and mount points for Widows and
        # Linux
        driveMountPoints = {'darwin': '/Volumes',
                            'linux platform name here': '/mnt',
                            'windows platform name here': 'mount point here',
                            }
        # Look up the mount point for this platform
        mountPoint = driveMountPoints[sys.platform]

        # Find all drives mounted on the mount point.
        mountedVolumes = []
        items = os.listdir(mountPoint)
        for item in items:
            item = os.path.join(mountPoint, item)
            if os.path.isdir(item):
                mountedVolumes.append(item)

        return mountedVolumes

    def enable(self, name, path):
        """Put the JSON token on this volume's root so OSP knows to
        pay attention to it and knows what name to use for it."""

        tokenFile = os.path.join(path, ospVolumeTokenName)

        # Check the provided volume path against the volumes known to be
        # avalable.
        if path not in self._mountedVolumes():
            # TODO: compare common roots and offer a suggestion in the error
            # message
            err_mess = "%s is not a valid path to a volume's root directory." \
                            % path
            raise Exception(err_mess)

        # TODO: Make sure we're not clobbering an existing JSON token!

        data = {u'name': name,
                u'path': path,
                }
        json.dump(data, file(tokenFile, 'w'), sort_keys=True, indent=4)

        self.reload()


class Volume(object):

    def __init__(self, name, path):
        self.path = path
        self.name = name

    def __repr__(self):
        return u'Volume: ' + self.name + u': ' + self.path


class Job(object):
    """
    Specify a show, sequence, shot, and task. Only show is mandatory. 
    
    Show, sequence and shot are heirarchical, a show has sequences, sequences 
    have shots. A Task is related to a show, but not to a specific sequence or shot.
    
    """
        
    def __init__(self, show=None, sequence=None, shot=None, task=None):
        """
        Arguments must be Show, Sequence, Shot, or Task objects from osp.core. 
        Show is mandatory, all others are optional.       
        
        >>> show = Show('Example Show')
        >>> shot = Shot('ab123')
        >>> job = Job(show, shot)
        >>> print job
        Job: {Show: Example Show, Shot: ab123}
        """
        
        assert type(show) == Show
        self.show = show
        self.sequence = None
        self.shot = None
        self.task = None
        # Optional arguments
        if sequence is not None:
            print "sequence:", sequence
            assert type(sequence) == Sequence
            self.sequence = sequence
        if shot is not None:
            print "shot:", shot
            assert type(shot) == Shot
            self.shot = shot
        if task is not None:
            print "task:", task
            assert type(task) == Task
            self.task = task    

    def __repr__(self):
        repr = u"Job: {" + str(self.show)
        for value in (self.sequence, self.shot, self.task):
            if value is not None:
                repr += ", " + str(value)
        repr += "}"
        return repr
    
    def getShow(self):
        return self.show
    
    def getSequence(self):
        return self.sequence
    
    def getShot(self):
        return self.shot
    
    def getTask(self):
        return self.task
        

class Environment(object):
    """
    
    """
    
    def __init__(self, job):
        """
       
        """

        assert type(job) == osp.core.Job
        self.job = job
        # Container for all the bits
        self._env = []
        # Load studio setup
        
        # Load show setup
        
        # Load sequence setup
        
        # Load shot setup
        
        # Load task setup
        
                
    def __add__(self, other):
        raise Exception('Not finished. Or started, really.')
        
    def __repr__(self):
        return str([type(thing) for thing in self._env])
        
    def setJob(self, job):
        self.__init__(job)
    
    def getJob(self):
        return self.job
        
    def filesystemPath(self, obj, volume):
        """
        Return the path to the directory on the given volume that represents obj.
        
        """
        
        assert type(volume) == osp.core.Volume
        raise Exception('Not done!')
        



def shows():
    """
    Return a list of all the shows available on local OSP-enabled volumes.

    """

    shows = []
    for volume in Volumes():
        for show in os.listdir(volume.path):
            shows.append(show)

    return shows



# Testing

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    



"""
Here's how I'd like stuff to work.


objects:
osp.Environment()
    volumes()  -- osp-enabled volumes
    job()
    sequence()
    shot()
    task()

osp.Volumes()
    load() -- find all osp-enabled volumes on this machine

osp.Volume()
    path
    name

osp.Job()
    name - full name
    path
    code - abbreviated name for filesystem
    readConfigFile() -- load configuration from JSON config file

"""

##
## Globals
##


#volumes = env.Volumes()

##
## From the alpha v0.001 of OSP:

"""
#! /usr/bin/python
#
# osp.py
#
# Module to contain central stuff used in all the osp* scripts.
#

import os

# Globals
job_envars = { 'OSP_JOB_PATH':'Job Path',
           'OSP_JOB_CODE':'Job Code',
           'OSP_JOB_NAME':'Job Name',
           'OSP_SEQ_PATH':'Sequence Path',
           'OSP_SEQ_NAME':'Sequence Name',
           'OSP_SHOT_PATH':'Shot Path',
           'OSP_SHOT_NAME':'Shot Name', }

job_folder_name = 'jobs'
job_osp_folder_name = '_osp'
job_config_file_name = 'osp_show_config.py'

osp_vols = os.getenv('OSP_VOLS')


##
## Methods
##

def volumes():
    "    Return a list of all OSP-enableled volumes available on this machine."

    return [vol for vol in osp_vols.split(':') if os.path.exists(vol)]

def job_dirs():
    "
    Return a list of the paths to all jobs folders on all the OSP-enableled
    volumes available on this machine.
    "

    dirs = [os.path.join(vol, job_folder_name) for vol in volumes()]
    return [dir for dir in dirs if os.path.exists(dir)]


def jobs():
    "
    Return a list of the paths to all OSP-enableled jobs available on this
    machine.
    "

    joblist = []
    for jobd in job_dirs():
        joblist += [os.path.join(jobd, d) for d in os.listdir(jobd)]
    return [job for job in joblist if os.path.exists(job_config_file(job))]


def job_config_file(job_path):
    "
    Accept the path to a job's root directory and return the path to that job's
    config file (whether or not it exists.)
    "

    return os.path.join(job_path, job_osp_folder_name, job_config_file_name)

def job_env(which=None):
    "
    Return a dictionary of environment variable names and their values for all
    job-related OSP evironment variables. If which is provided, filter out the
    variable names that don't conatain the value of which.
    "

    out = {}
    for var in job_envars:
        if which and which not in var: continue
        if os.getenv(var) is not None: out[var] = os.getenv(var)
    return out



if __name__ == "__main__":
    pass


"""
