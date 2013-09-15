#Open Source Pipeline

##Mission: 
It's the twenty-first century, folks! If you're working in the VFX industry, there's a good chance you're not working at ILM, DD, Weta or any other shop that's been around for ages and has lots of developers working on their big, well-funded pipeline. In fact, it's very likely that you're part of a small team leveraging the current peak of capability found in commodity hardware and the wealth of non-proprietary VFX software to create your own world. And why wouldn't you? 

The problem you're probably running into -- just like every other small shop -- is that these commodity tools don't automatically slot into each-other by themselves. And moving information around by hand is definitely sub-optimal. You may have also teamed up with other small shops and need to be able to swap files around between yourselves.

So you need a little bit of organization and you need a little bit of glue-ware. 

Enter the Open Source Pipeline.

##Current status: Redesign in progress
OSP ran into a dead-end trying to be too tricky and too reliant on BASH, so I'm in the midst of a redesign. This requires that I do some learning and question some of my basic assumptions, too. Frankly, that's the whole point of this little project anyway. Expect the goals and approach to evolve as I make progress. So far, I have the base framework sketched out as Python objects. Now it's time to plan how these objects relate to each-other and to the real world (or, less dramatically, the filesystem and/or the production database.) 

Special thanks goes out to Mateusz Wójt for getting in touch about why OSP wasn't working. I had left OSP in a totally broken state for nearly a year -- not good! That spurred some re-thinking and this new approach. 

##Goals:
+ Understand that artists want to deal with as little "technical stuff" as possible.
+ Minimal configuration on the workstation.
    + Require Python 2.7
    + Insert a path to OSP in site-packages.
+ Structure the environment so that it's flexible and expandable (multiple shows, variable naming-standards, changing storage).
+ Allow customization.
    + Facilitate overloading OSP standard components with local studio-custom code. 
+ Be flexible about what database (if any) will be used. (I do truly love Shotgun, but some people may not need or want to be tied to it. Some studios may not even need a database at all.)
+ Facilitate "breaking off" a chunk of work to outside vendors and bringing their output back into the pipe. 

##Approach:
+ Use Python objects to represent the logical structure at a facility, for it's resources and  it's projects.
+ Provide interfaces from that logical structure to the actual tools used. (Shells or a GUI, DCC apps, filesystem(s), database, renderfarm)
+ Use the idea from Unix of simple, single-function tools, piped together to create something useful and complex.
+ Artists' jobs are hard enough. If you make it easy for them to do the "right thing," they will. If it's complicated, they won't. Let's make it easy so we can all have a nicer time. We can do this by chosing intelligent defaults and by integrating OSP into DCC applications in a way that's consistent with the application's workflow.

##Components (no longer) in progress (due to the redesign):
+ ospenv : A studio-wide command-line environment and framework for job-specific customizations. This is the base framework that OSP will run on. 
+ show.sh : Allows the user to further set up the environment for a show, sequence and shot.

##Future components:
+ Daily system
+ Site/Show/Shot magic for Nuke. Knobs in root which get evaluated + updated, all pathnames in script get expression-linked to the root knobs for single-point "correctability."
+ A publishing system to "nail down" files and avoid unexpected changes downstream.
+ A "package up these files and send them to a vendor" tool.

###Things that are specifically related to Shotgun:
+ Check-in tool for logging sources in SG.
+ Log all sources in a Nuke script into Shotgun as an element and link them to the SG Version.

##Installing
1. Prereqs: You'll need to be running Python 2.7.
2. Grab the .zip from [GitHub](https://github.com/timbowman/OpenSourcePipeline).
3. Unzip it and copy it to your centralized location for scripts at your studio. (For me, that's "/Volumes/OSP-Test-Disk/studio/scripts/".)
4. In a terminal, switch to the directory where you just put OSP and run install.py.

    $ cd /Volumes/OSP-Test-Disk/studio/scripts/OpenSourcePipeline-master
    $ ./install.py

5. Now you can start Python and import osp.
    
    $ python
    Python 2.7.3 (v2.7.3:70274d53c1dd, Apr  9 2012, 20:32:06)
    [GCC 4.0.1 (Apple Inc. build 5493)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import osp
    >>>

6. Now it's time to tell OSP where my files are stored.

    >>> osp.Volumes().enable('MyFiler', '/Volumes/OSP-Test-Disk')

This puts a JSON file (`osp-volume.json`)in the root of my test disk. OSP will look for a file like this one in the root of each mounted volume.

    >>>exit()
    $ cat /Volumes/OSP-Test-Disk/osp-volume.json
    {
        "name": "MyFiler",
        "path": "/Volumes/OSP-Test-Disk"
    }%                                                                            

7. Now, back in Python, OSP knows where I store my data.

    $ python
    Python 2.7.3 (v2.7.3:70274d53c1dd, Apr  9 2012, 20:32:06)
    [GCC 4.0.1 (Apple Inc. build 5493)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import osp
    >>> osp.Volumes()
    [Volume: MyFiler: /Volumes/OSP-Test-Disk]
    >>>

