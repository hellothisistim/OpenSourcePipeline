
import os

showname = os.getenv('OSP_SHOW_NAME')
showdir = os.getenv('OSP_SHOW')
seqname = os.getenv('OSP_SEQ_NAME')
seqdir = os.getenv('OSP_SEQ')
shotname = os.getenv('OSP_SHOT_NAME')
shotdir = os.getenv('OSP_SHOT')

if showname and showdir:
    nuke.addFavoriteDir(showname, showdir)
if seqname and seqdir:
    nuke.addFavoriteDir(' ' + seqname, seqdir)
if showname and showdir:
    nuke.addFavoriteDir(' ' + seqname + shotname, shotdir)
    
    # Add shortcuts for plates/comps/elements