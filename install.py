#
# install
#
"""
Installs Open Source Pipeline (OSP) on the local computer.

OSP puts it's one "hook" into a computer's configuration via
Python's site-packages. [http://docs.python.org/library/site.html]
This script will add or update a path configuration file
("osp.pth") in the first available site-packages directory on the
local system, allowing the osp module to be imported in Python.
"""

# From Python
import logging
import os
import site
import sys
from optparse import OptionParser

## ---------------------------------------------------------------------
## GLOBALS
## ---------------------------------------------------------------------

path_config_filename = 'osp.pth'


#Set up logging
logging.basicConfig()
#log = logging.getLogger(__file__)
log = logging.getLogger()
log.setLevel(level=logging.INFO)
# TODO: Logging info should be saved to a install.log file.
# But where? In the same directory as install.py? In ~? ~/.osp?


## ---------------------------------------------------------------------
## METHODS
## ---------------------------------------------------------------------

def find_install_location():
    """
    Search the list of all the possible locations for site-packages for
    one that actually exists on the local machine. Return the first one 
    found.
    """

    pkgs = site.getsitepackages()
    for location in pkgs:
        if os.path.exists(location):
            return location
    # Didn't find one. Better throw an error.
    # (Is it even possible for this to happen? tb)
    raise Exception("No site-packages directory found on this system. \
    Tried these locations and none exist: %s" % ", ".join(pkgs))


def install(location):
    """
    Replace any existing osp.pth file in the install location with a new one.
    """

    # TODO: Should probably remove any existing osp.pth files from _any_
    # site-packages dirs in site.getsitepackages()
    # TODO: We should be checking for Python 2.7 because this site-packages 
    # shenanigans won't work on anything earlier.
    log.debug('Starting installation to %s' % location)
    # Assume this script is in the root of the OSP install.
    osp_dir = os.path.dirname(os.path.abspath(__file__))
    log.debug('OSP home is %s' % osp_dir)
    file_contents = """# Open Source Pipeline\n%s\n""" % osp_dir
    path_config_file = os.path.join(location, path_config_filename)
    log.debug('Writing path configuration file to %s' % path_config_file)
    out = open(path_config_file, 'w')
    out.write(file_contents)
    out.close()
    log.debug('Installation finished.')


def remove():
    """
    Remove any existing osp.pth file from any path in site.getsitepackages().
    """

    log.debug('Starting removal.')    
    for directory in site.getsitepackages():
        path_file = os.path.join(directory, path_config_filename)
        if os.path.exists(path_file):
            log.debug('Removing %s' % path_file)
            os.remove(path_file)
    log.debug("Removal finished.")


## ---------------------------------------------------------------------
## MAIN
## ---------------------------------------------------------------------

if __name__ == '__main__':

    parser = OptionParser(usage="""install [options]

    Install Open Source Pipeline (OSP) on this computer.

    Enables OSP on the local machine by adding a path configuration file
    ("osp.pth") to Python's site-packages directory. Requires Python 2.7 
    or later.""")
    parser.add_option('-v', '--verbose', action='store_true', dest='verbose',
                      default=False, help='Verbose')
    parser.add_option('-r', '--remove', action='store_true', dest='remove',
                      default=False, help='Remove OSP configuration')

    (options, args) = parser.parse_args()
    if options.verbose:
        log.setLevel(level=logging.DEBUG)

    # Are we in Python 2.7 or later?
    log.debug('Running in Python version: %s' % sys.version)
    py_major, py_minor = sys.version_info[0:2]
    if py_major < 2 or py_minor < 7:
        sys.exit('Error: OSP must be installed using Python 2.7 or later.')
    
    if options.remove:
        remove()
    else:
        install(find_install_location())
