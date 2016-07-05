#!/usr/bin/python

import os
import sys
import re

def error_exit(msg):
  print "Error: "+msg
  sys.exit()

def mod_file(line,file):
  x = line.split("==")
  x[1] = " "+file
  line = "==".join(x)
  line = line + "\n"
  return line

def mod_ntimes(line,val):
  x = line.split("==")
  x[1] = int(x[1]) + int(val)
  x[1] = " "+str(x[1])
  line = "==".join(x)
  line = line + "\n"
  return line

def mod_dt(line,val):
  x = line.split("==")
  x[1] = " "+val
  line = "==".join(x)
  line = line + "\n"
  return line

case_name = os.environ['CASE_NAME']
r_num = os.environ['R_NUM']
p_num = int(r_num)-1
p_num = str(p_num)
p_num = p_num.zfill(3)
d_ntimes = os.environ['D_NTIMES']
dt = os.environ['DT']

inifile = os.environ['WORK_DIR'] + "/out/" + case_name + ".r." + p_num + ".nc"
rstfile = os.environ['WORK_DIR'] + "/out/" + case_name + ".r." + r_num + ".nc"
hstfile = os.environ['WORK_DIR'] + "/out/" + case_name + ".h." + r_num + ".nc"
avgfile = os.environ['WORK_DIR'] + "/out/" + case_name + ".a." + r_num + ".nc"

infile =case_name+'_'+p_num+'.in'
outfile=case_name+'_'+r_num+'.in'

if not os.path.isfile(infile):
  msg = infile+" does not exist."
  error_exit(msg)
if os.path.isfile(outfile):
  msg = outfile+" has already exist."
  error_exit(msg)

fi0 = open(infile ,'r')
fo0 = open(outfile,'w')

for line in fi0:
  if not re.match(r'^!',line):
    if   re.match(r'^\s*ININAME\s*==',line):
      line = mod_file(line, inifile)
    elif re.match(r'^\s*RSTNAME\s*==',line):
      line = mod_file(line, rstfile)
    elif re.match(r'^\s*HISNAME\s*==',line):
      line = mod_file(line, hstfile)
    elif re.match(r'^\s*AVGNAME\s*==',line):
      line = mod_file(line, avgfile)
    elif re.match(r'^\s*NTIMES\s*==',line):
      line = mod_ntimes(line, d_ntimes)
    elif re.match(r'^\s*DT\s*==',line):
      line = mod_dt(line, dt)
  fo0.write(line)
  
fi0.close()
fo0.close()
