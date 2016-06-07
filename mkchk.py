#!/usr/bin/python

import os
import re

def line_strip1(l,n):
  l = l.rstrip()
  l = l.split("=")
  l = l[n].strip()
  l = l.split("!")
  l = l[0].strip()
  return l

def line_strip2(l,n):
  l = l.rstrip()
  l = l.split("==")
  l = l[n].strip()
  l = l.split("!")
  l = l[0].strip()
  return l

case_name = os.environ['CASE_NAME']
r_num = os.environ['R_NUM']

infile=case_name+'_'+r_num+'.in'

fi0 = open(infile,'r')

for line in fi0:
  if not re.match(r'^!',line):
    if 'TITLE' in line:
      item = line_strip1(line,0)
      val  = line_strip1(line,1)
      print "{0:<12}: {1:<12}".format(item, val)
    if 'NtileI' in line or 'NtileJ' in line or 'NTIMES' in line or 'DT' in line or 'NDTFAST' in line or 'NRST' in line or 'NINFO' in line or 'NHIS' in line or 'NAVG' in line or 'NDIA' in line or 'TNU2' in line or 'VISC' in line or 'AKT' in line or 'AKV' in line or 'NUDG' in line or 'RSTNAME' in line or 'HISNAME' in line or 'AVGNAME' in line:
      item = line_strip2(line,0)
      val  = line_strip2(line,1)
      print "{0:<12}: {1:<12}".format(item, val)

fi0.close()
