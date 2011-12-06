#!/usr/bin/python

#pylint: disable-msg=E0012

import os
import shutil
import subprocess
import sys


BASE_HEADER = "# Generated by the protocol buffer compiler.  DO NOT EDIT!"
PYLINT_IGNORE = "\n\n#pylint: disable-msg=F0401,W0311,R0903,W0232,W0611,W0301"
PYDEV_IGNORE = "\n#@PydevCodeAnalysisIgnore"
NEW_HEADER = BASE_HEADER + PYLINT_IGNORE + PYDEV_IGNORE
OUTPUT_FILE = 'models_pb2.py'


def fix_protobuf_warnings():
    with open(OUTPUT_FILE, 'r') as models:
        models_text = models.read()
    with open(OUTPUT_FILE, 'w') as models:
        models.write(models_text.replace(BASE_HEADER, NEW_HEADER))


subprocess.call("protoc --python_out=. *.proto", shell=True)
print "Fixing protobuf warning crap..."
fix_protobuf_warnings()

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dest_path = os.path.join(parent_dir, 'fluidity/models.py')
print "Moving generated model proto file to: " + dest_path
shutil.move('models_pb2.py', dest_path)
