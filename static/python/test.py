#!/usr/bin/env python

import os
import sys

if len(sys.argv) > 1:
  output = sys.argv[1]
else:
  output = "no argument found"

print "Hello World!!!"
print output