#!/usr/bin/env python

import os
import sys
import tempfile

import PIL
import PIL.Image

MAX_SIZE = 2 * 1024 * 1024
MIN_SIZE = int(MAX_SIZE * 0.9)
QUALITY = 90

origFilename = sys.argv[1]
tempFilename = '/tmp/' + next(tempfile._get_candidate_names())
print tempFilename

img = PIL.Image.open(origFilename)
size = os.path.getsize(origFilename)

c = 1

while True:
    print("size = %s" % size)
    if size < MIN_SIZE:
        print("<")
        c = (c + 1) / 2.0
    elif size <= MAX_SIZE:
        print("=")
        name, ext = os.path.splitext(origFilename)
        img.save(name + '_2mb' + ext, "JPEG", quality = QUALITY)       
        break
    else:
        print(">")
        c = c / 2.0
    print("c = %s" % c)
    img = PIL.Image.open(origFilename)
    img = img.resize((int(img.size[0] * c), int(img.size[1] * c)), PIL.Image.ANTIALIAS)
    img.save(tempFilename, "JPEG", quality = QUALITY)
    size = os.path.getsize(tempFilename)


