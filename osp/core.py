
import json
import os
import sys

# TODO: add logging

## Globals


## ---------------------------------------------------------------------
## Classes
## ---------------------------------------------------------------------
        


# TODO: Once we've set up the environment, we'll build objects like this 
# to hand around. It'll be awesome.
class Image(object):
    """
    Yup, it's a picture. It has height & width, type and a filepath.
    """
    
    pass

class ImageSequence(object):
    pass
    
class Mesh(object):
    """
    A 3D mesh. Should probably investigate Alembic before we implement 
    this. No sense duplicating effort. There may be something useful there.
    """
    
class ApplicationVersion(object):
    """
    Represents a specific version of an application.
    (For example, Nuke version6.3v6)
    
    """
    
    pass
    

if __name__ == "__main__":
    
    show = Show('test')
    seq = Sequence('sample')
    env = Environment(show=show, sequence=seq)
    print env