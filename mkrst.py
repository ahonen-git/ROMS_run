#!/usr/bin/python

import os
import sys
import re

def error_exit(msg):
  print "Error: "+msg
  sys.exit()

def mod_ini(line,rst):
  x = line.split("==")
  print x[0], x[1]
  x[1] = " "+rst+"\n"
  print x[0], x[1]
  line = "==".join(x)
  return line

case_name = os.environ['CASE_NAME']
r_num = os.environ['R_NUM']
p_num = int(r_num)-1
p_num = str(p_num)
p_num = p_num.zfill(3)

rstfile = os.environ['WORK_DIR'] + "/out/" + case_name + ".r." + p_num + ".nc"

infile =case_name+'_'+p_num+'.in'
outfile=case_name+'_'+r_num+'.in'

if not os.path.isfile(infile):
  msg = infile+" does not exist."
  error_exit(msg)
if os.path.isfile(outfile):
  msg = outfile+" has already exist."
  error_exit(msg)
if not os.path.isfile(rstfile):
  msg = rstfile+" does not exist."
  error_exit(msg)

fi0 = open(infile ,'r')
fo0 = open(outfile,'w')

for line in fi0:
  if not re.match(r'^!',line):
    if 'ININAME'   in line:
      line = mod_ini(line, rstfile)
    elif 'RSTNAME' in line:
      line = line.replace(p_num,r_num)
    elif 'HISNAME' in line:
      line = line.replace(p_num,r_num)
    elif 'AVGNAME' in line:
      line = line.replace(p_num,r_num)
  fo0.write(line)
  
fi0.close()
fo0.close()
