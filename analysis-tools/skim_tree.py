#! /usr/bin/env python

import os, pickle, sys, ROOT, logging
ROOT.gROOT.SetBatch(True)
from optparse import OptionParser
# FIXME: this will not work unless it is in heppynmore python directory.
sys.path.append('/afs/cern.ch/user/b/bortigno/workspace/heppynmore-dev/python/')
from myutils import copytree

argv = sys.argv

#get files info from config
parser = OptionParser()
parser.add_option("-F", "--filein", dest="fileIN", default="",
                      help="input file")
parser.add_option("-I", "--pathin", dest="pathIN", default="",
                      help="input directory")
parser.add_option("-O", "--pathout", dest="pathOUT", default="",
                              help="pathOUT")
parser.add_option("-C", "--cut", dest="cut_string", default="",
                              help="cut string")
parser.add_option("-P","--outputfile-prefix",dest="output_prefix",default="",
                  help="String prefix for outoutfile")
(opts, args) = parser.parse_args(argv)

if not (opts.fileIN == ""):
  copytree(os.path.dirname(os.path.abspath(opts.fileIN)),opts.pathOUT,'',opts.output_prefix,os.path.basename(opts.fileIN),'',opts.cut_string)
else:
  for f in os.listdir(opts.pathIN):
    if not f.endswith('.root'): continue
    copytree(opts.pathIN,opts.pathOUT,'',opts.output_prefix,os.path.splitext(f)[0],'',opts.cut_string)
