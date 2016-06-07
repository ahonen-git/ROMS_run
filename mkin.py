#!/usr/bin/python

import os

case_name = os.environ['CASE_NAME']
r_num = os.environ['R_NUM']

outfile=case_name+'_'+r_num+'.in'

fi0 = open('template_001.in','r')
fo0 = open(outfile,'a')

for line in fi0:
  line = line.replace('${CASE_NAME}',case_name)
  line = line.replace('${R_NUM}'    ,r_num)
  fo0.write(line)
  
fi0.close()
fo0.close()

#txt = fi0.readlines()
#fi0.close()
#
#for line in txt:
