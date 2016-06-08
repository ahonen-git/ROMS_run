#!/usr/bin/python

import os

case_name = os.environ['CASE_NAME']
r_num = os.environ['R_NUM']
d_ntimes = os.environ['D_NTIMES']
dt = os.environ['DT']

outfile=case_name+'_'+r_num+'.in'

fi0 = open('template.in','r')
fo0 = open(outfile,'a')

for line in fi0:
  line = line.replace('${CASE_NAME}',case_name)
  line = line.replace('${R_NUM}'    ,r_num)
  line = line.replace('${D_NTIMES}' ,d_ntimes)
  line = line.replace('${DT}'       ,dt)
  fo0.write(line)
  
fi0.close()
fo0.close()
