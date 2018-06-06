#! /usr/bin/env python

import os, pickle, sys, ROOT, logging
ROOT.gROOT.SetBatch(True)
from optparse import OptionParser
# FIXME: this will not work unless it is in heppynmore python directory.
from myutils import copytree

argv = sys.argv

#get files info from config
parser = OptionParser()
parser.add_option("-I", "--pathin", dest="pathIN", default="",
                      help="input directory")
parser.add_option("-O", "--pathout", dest="pathOUT", default="",
                              help="pathOUT")
parser.add_option("-C", "--cut", dest="cut_string", default="",
                              help="cut string")
(opts, args) = parser.parse_args(argv)

for f in os.listdir(opts.pathIN):
    if not f.endswith('.root'): continue
    copytree(opts.pathIN,opts.pathOUT,'','',os.path.splitext(f)[0],'',opts.cut_string)
