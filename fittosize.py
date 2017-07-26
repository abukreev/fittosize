#!/usr/bin/env python

import os
import sys
import tempfile

MAX_SIZE = 2 * 1024 * 1024

origFilename = sys.argv[1]
tempFilename = '/tmp/' + next(tempfile._get_candidate_names())
size = os.path.getsize(origfilename)
while (size > MAX_SIZE):
    size = os.path.getsize(tempFilename)

print tempFilename
