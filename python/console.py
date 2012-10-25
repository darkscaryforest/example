#!/usr/bin/python

import commands

print "1. Do an ls.  Returns 2-tuple with status of command and command output"
cmd = commands.getstatusoutput("ls")
print cmd

print "2. Do an ls.  Return just command output."
cmd = commands.getoutput("ls")
print cmd
