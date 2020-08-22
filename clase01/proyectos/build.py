#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import hashlib
import time

cmd = "pandoc -t beamer slides.md -o slides.pdf"

checksum = None

print "\n".join(os.listdir("imgs"))
print "*" * 10

while True:

    with open("slides.md") as fp:
        newchecksum = hashlib.sha1(fp.read()).hexdigest()

    if newchecksum != checksum:
        print "building"
        os.system(cmd)
        checksum = newchecksum



    time.sleep(2)
