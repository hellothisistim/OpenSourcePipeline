#
# core.py
#
# Tim BOWMAN [puffy@netherlogic.com]
#


import json
import os
import sys

# TODO: add logging

## Globals
ospVolumeTokenName = u'osp-volume.json'  # indicates an OSP-enabled volume.
jobDirName = 'jobs'
jobConfigFileName = 'osp_show_config.json'


## ---------------------------------------------------------------------
## Classes
## ---------------------------------------------------------------------

class Environement(object):
    """We'll be setting the whats and wherefores for the OSP job
    environment here. With any luck, we'll be able to pickle these and
    then pass them around. And also pass them to the shell-specific
    scripts so the environment can be set in whatever shell we
    like... bash or zsh or maybe even DOS!
    """

    def __init__(self):
        # find OSP-enabled volumes
        self.volumes = Volumes()
        # look for local studio configs
        pass
        # set up aliases for applications
        pass


class Job(object):
    """Represents a job (a.k.a. show, commercial, project, film, etc.)
    in OSP.

    """

    """
    self.meta = { 'OSP_JOB_PATH':u'Job Path',
             'OSP_JOB_CODE':u'Job Code',
             'OSP_JOB_NAME':u'Job Name',
             }
    """

    def __init__(self, code, fullName=None):
        self.code = code  # Job code name
        self.fullName = fullName  # Job's full name
        self.sequences = list()

    #def __repr__(self):
    #    reprString = u"Job: " + self['code']
    #    if self['fullName'] is not None:
    #        reprString += u', ' + self['fullName']
    #    return reprString
    #
    ## Loading all the sequences in a job isn't so easy -- where do we
    ## load it from? Filesystem? Database?
    #def _loadSequences(self):
    #    sequences = []
    #    return sequences


class Sequence(object):
    """Represents a sequence in OSP."""

    meta = {'OSP_SEQ_PATH': u'Sequence Path',
            'OSP_SEQ_NAME': u'Sequence Name',
            }

    def __init__(self, code, fullName=None):
        self.code = code
        self.fullName = fullName
        self.shots = []

    def __repr__(self):
        reprString = u"Sequence: " + self.code
        if self.fullName is not None:
            reprString += u', ' + self.fullName
        return reprString


class Shot(object):

    meta = {'OSP_SHOT_PATH': 'Shot Path',
            'OSP_SHOT_NAME': 'Shot Name',
            }

    def __init__(self, code, fullName=None):
        self.code = code
        self.fullName = fullName

    def __repr__(self):
        reprString = u"Shot: " + self.code
        if self.fullName is not None:
            reprString += u', ' + self.fullName
        return reprString


# TODO: Maybe make a Task class?
class Task(object):
    pass


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
                import json
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
        json.dump(data, file(tokenFile, 'w'))

        self.reload()


class Volume(object):

    def __init__(self, name, path):
        self.path = path
        self.name = name

    def __repr__(self):
        return u'Volume: ' + self.name + u': ' + self.path
