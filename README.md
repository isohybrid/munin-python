munin-python
============

learn from http://tomoconnor.eu/blogish/monitoring-munin/#.UZsHuqDLVk9

monitor system through munin with python plugins 


If you have multiple munin-servers, or want to retrieve munin-plugin data from Nagios servers, then you can add multiple “allow” regex lines.  
 
So.. Munin plugins.  This is the Really Cool Stuff.
You can write munin plugins in any language you like.  The vast majority on Munin Exchange  are written in Perl or Bash.  I prefer writing in Python, and the munin-python module is gorgeous.  
Basically, you need to handle two things, “config” and “run” modes.  
Munin-run is the thing that handles the plugin, and runs “your-plugin config”.  This is what defines the format of the RRD files that munin uses to generate graphs.  OK, so let’s look at a simple munin plugin.  I think we’ll monitor... the number of files in /tmp (well, why not?)

notes:
    try to get used to the command "munindoc, munin-check, munin-run, munin-cron, munin-node, munin-node-configure"

    may need use the command "munin-check -f" to fix some error
    

    On the host where Munin runs, run munin-update as the munin user account.
    This step will tell you whether munin-update(the server) is able to communicate with munin-node(the agent).

    su -s /bin/bash munin  or   su - munin --shell=/bin/bash
    usr/share/munin/munin-update --debug --nofork --host foo.example.com --service df
