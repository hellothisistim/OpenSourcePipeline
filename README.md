#Open Source Pipeline

##Mission: 
It's the twenty-first century, folks! If you're working in the VFX industry, there's a good chance you're not working at ILM, DD, Weta or any other shop that's been around for ages and has lots of developers working on their big, well developed pipeline. In fact, it's very likely that you're part of a small team leveraging the current peak of capability found in commodity hardware and the wealth of non-proprietary VFX software to create your own world. And why wouldn't you? 

The problem you're probably running into -- just like every other small shop -- is that these commodity tools don't automatically slot into each-other by themselves. And moving information around by hand is definitely sub-optimal. You may have also teamed up with other small shops and need to be able to swap files around between yourselves.

So you need a little bit of organization and you need a little bit of glue-ware. 

Enter the Open Source Pipeline.

##Current status: Foundation work
I have the base framework sketched out as Python objects. Now it's time to plan how these objects relate to the real world (or, less dramatically, the filesystem and/or the production database.)

Special thanks goes out to Mateusz Wójt for getting in touch about why OSP wasn't working. I had left OSP in a totally broken state for nearly a year -- not good! That spurred some re-thinking and this new approach. 

##Goals:
+ Minimal configuration on the workstation
+ Understand that artists want to deal with as little "technical stuff" as possible. 
+ Structure the environment so that it's flexible and expandable (multiple shows, variable naming-standards, changing storage).
+ Utilize Shotgun as a central "brain" that knows where everything lives on the filesystem. 
+ Facilitate "breaking off" a chunk of work to outside vendors and bringing their output back into the pipe. 
+ Allow customization by overloading OSP standard components with local studio-custom code. 

##Approach: 
+ Use the idea from Unix of simple, single-function tools, piped together to create something useful and complex.
+ Rely on [Shotgun](http://www.shotgunsoftware.com/) for the production database.

##Components in progress:
+ ospenv : A studio-wide command-line environment and framework for job-specific customizations. This is the base framework that OSP will run on. 
+ show.sh : Allows the user to further set up the environment for a show, sequence and shot.

##Future components:
+ Daily system
+ Site/Show/Shot magic for Nuke. Knobs in root which get evaluated + updated, all pathnames in script get expression-linked to the root knobs for single-point "correctability."
+ Checking  tool for logging sources in SG.
+ Log all sources in a Nuke script into Shotgun as an element and link them to the SG Version.
+ A "package up these files and send them to a vendor" tool.

#Installing

The Open Source Pipeline will need to have a home on a central location, called OSP_HOME. This will probably be a network share or something similar, something that's available to all the machines in the facility. 

Once the OSP files are placed in this central location, run the install script (osp/core/ospinstall) on each machine that will be "OSP-aware." This script will modify /etc/bashrc in order to source the OSP environment from our central location. This is the only bit of configuration that lives locally on a workstation (see goal #1, "minimal configuration on the workstation," above.) All other configuration will be done facility-wide from OSP_HOME.
