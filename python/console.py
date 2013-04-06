#!/usr/bin/python

import commands, os

print "1. Do an ls.  Returns 2-tuple with status of command and command output"
cmd = commands.getstatusoutput("ls")
print cmd

print "2. Do an ls.  Return just command output.\nNote that this does not spawn a new process\n(python \"pauses\" until completion of command)."
cmd = commands.getoutput("ls")
print cmd

print "3. To start a command in the background, we use os.system"
os.system("echo \"this is an echo\" process &")
