#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os, os.path

cmd = "../../app-stores-toolkit/populate.py metadata -platform android -prj-path gplay -data-file-path src/goldminer-classic-origin-metadata-translate.xlsx -customized-metadata-path src/gplay/metadata"
print cmd
os.system(cmd)
