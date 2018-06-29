#!/usr/bin/env python
from __future__ import print_function
import json
import sys


"""
Quick script to extract the field "text" in json file to print to STDOUT

Example Usage: gettext.py 1965.471-t01.json
"""

with open(sys.argv[1], 'r') as jf:
    data = json.loads(jf.read())

if 'transcript' not in data or data['transcript'] is None \
        or 'sections' not in data['transcript']:
    sys.exit(1)

for s in data['transcript']['sections']:
    for t in s['turns']:
        for textblock in t['text_blocks']:
            print(textblock['text'])
