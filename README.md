#Open Source Pipeline

##Mission: 
It's the twenty-first century, folks! If you're working in the VFX industry, there's a good chance you're not working at ILM, DD, Weta or any other shop that's been around for ages and has lots of developers working on their big, well developed pipeline. In fact, it's very likely that you're part of a small team leveraging the current peak of capability found in commodity hardware and the wealth of non-proprietary VFX software to create your own world. And why wouldn't you? 

The problem you're probably running into -- just like every other small shop -- is that these commodity tools don't automatically slot into each-other by themselves. And moving information around by hand is definitely sub-optimal. You may have also teamed up with other small shops and need to be able to swap files around between yourselves.

So you need a little bit of organization and you need a little bit of glue-ware. 

Enter the Open Source Pipeline.

##Current status: Redesign
OSP ran into a dead-end trying to be too tricky and too reliant on BASH, so I'm in the midst of a redesign. This requires that I do some learning and question some of my basic assumptions, too. Frankly, that's the whole point of this little project anyway. Expect the goals and approach to evolve as I make progress. So far, I have the base framework sketched out as Python objects. Now it's time to plan how these objects relate to each-other and to the real world (or, less dramatically, the filesystem and/or the production database.) 

Special thanks goes out to Mateusz Wójt for getting in touch about why OSP wasn't working. I had left OSP in a totally broken state for nearly a year -- not good! That spurred some re-thinking and this new approach. 

##Goals:
+ Minimal configuration on the workstation
+ Understand that artists want to deal with as little "technical stuff" as possible.
+ Structure the environment so that it's flexible and expandable (multiple shows, variable naming-standards, changing storage).
+ Be flexible about what database (if any) will be used. (I do truly love Shotgun, but some people may not need or want to be tied to it. Some studios may not even need a database at all.)
+ Facilitate "breaking off" a chunk of work to outside vendors and bringing their output back into the pipe. 
+ Allow customization by overloading OSP standard components with local studio-custom code. 

##Approach:
+ Use Python objects to represent the logical structure at a facility, for it's resources and  it's projects.
+ Provide interfaces from that logical structure to the actual tools used. (Shells or a GUI, filesystem(s), database, renderfarm)
+ Use the idea from Unix of simple, single-function tools, piped together to create something useful and complex.
+ Artists' jobs are hard enough. If you make it easy for them to do the "right thing," they will. If it's complicated, they won't. Let's make it easy so we can all have a nicer time. We can do this by chosing intelligent defaults and by integrating OSP into applications in a way that's consistent with that application's workflow.

##Components (no longer) in progress (due to the redesign):
+ ospenv : A studio-wide command-line environment and framework for job-specific customizations. This is the base framework that OSP will run on. 
+ show.sh : Allows the user to further set up the environment for a show, sequence and shot.

##Future components:
+ Daily system
+ Site/Show/Shot magic for Nuke. Knobs in root which get evaluated + updated, all pathnames in script get expression-linked to the root knobs for single-point "correctability."
+ A publishing system to "nail down" files and avoid unexpected changes downstream.
+ A "package up these files and send them to a vendor" tool.

Things that are specifically related to Shotgun:
+ Check-in tool for logging sources in SG.
+ Log all sources in a Nuke script into Shotgun as an element and link them to the SG Version.

