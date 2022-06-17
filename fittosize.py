#!/usr/bin/env python

import os
import shutil
import sys
import tempfile

import PIL
import PIL.Image

MAX_SIZE = 2 * 1024 * 1024
MIN_SIZE = int(MAX_SIZE * 0.9)
QUALITY = 90

ORIGINAL_FILENAME = sys.argv[1]
TMP_FILENAME = '/tmp/' + next(tempfile._get_candidate_names()) + os.path.splitext(ORIGINAL_FILENAME)[1]

def resize(c, q):
    img = PIL.Image.open(ORIGINAL_FILENAME)
    img = img.resize((int(img.size[0] * c), int(img.size[1] * c)), PIL.Image.ANTIALIAS)
    img.save(TMP_FILENAME, "JPEG", quality = q)
    size = os.path.getsize(TMP_FILENAME)
    return size

def save_result():
    name, ext = os.path.splitext(ORIGINAL_FILENAME)
    new_name = name + '_2mb' + ext
    shutil.move(TMP_FILENAME, new_name)

img = PIL.Image.open(ORIGINAL_FILENAME)
size = os.path.getsize(ORIGINAL_FILENAME)

qmin = 90
qmax = 100
q = 90
cmin = 0.1
cmax = 1.0
c = 1

if os.path.getsize(ORIGINAL_FILENAME) > MAX_SIZE:   
    for _ in range(0, 10):
        print("c = " + str(c) + ", q = " + str(q))
        size = resize(c, q)
        if size < MIN_SIZE:
            print("<")
            cmin = c
            qmin = q
            save_result()
        elif size <= MAX_SIZE:
            print("=")
            save_result()
            break
        else:
            print(">")
            cmax = c
            qmax = q
#        q = int((qmin + qmax) / 2.0)
        c = min(1.0, ((cmin + cmax) / 2.0) + 0.1)


