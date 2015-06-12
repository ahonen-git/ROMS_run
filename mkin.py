#!/usr/local/bin/python

import sys
import re

def set_dstart(l,dt):
  x = l.split('=')
  y = x[1].split('!')
  n0 = re.search(r'd',y[0])
  if n0:
    z = y[0].split('d')
    xxx = float(z[0])
  else:
    xxx = float(y[0])
  xxx = xxx + dt
  str="%s = %s ! %s" % (x[0], xxx, y[1])
  sys.stdout.write(str)

def add_cnt(l,sss):
  x = l.split(sss)
  y = x[1].split('.')
  xxx = int(y[0]) + 1
  str="%s%s%03i.%s" %(x[0],sss,xxx,y[1])
  sys.stdout.write(str)

def set_ini(l,arg):
  f = open(arg)
  for ll in f:
    n04 = re.search(r'RSTNAME',ll)
    n05 = re.search(r'^\!'    ,ll)
    if n04 and not n05:
      rst=ll.split('==')
      ini=l.split('==')
  str="%s%s%s" % (ini[0],'==',rst[1])
  sys.stdout.write(str)

dt = 1826.25

argvs = sys.argv
argc = len(argvs)

if (argc != 2):
  print 'Usage: python %s case_XXX.in ' % argvs[0]
  quit()

f0 = open(argvs[1])

for l in f0:
  n00 = re.search(r'DSTART',l)
  n01 = re.search(r'^\!'   ,l)

  n02 = re.search(r'ININAME',l)
  n03 = re.search(r'^\!'    ,l)

  n04 = re.search(r'RSTNAME',l)
  n05 = re.search(r'^\!'    ,l)

  n06 = re.search(r'HISNAME',l)
  n07 = re.search(r'^\!'    ,l)

  n08 = re.search(r'AVGNAME',l)
  n09 = re.search(r'^\!'    ,l)

  n10 = re.search(r'STANAME',l)
  n11 = re.search(r'^\!'    ,l)

  if   n00 and not n01:
    set_dstart(l,dt)

  elif n02 and not n03:
    set_ini(l,argvs[1])

  elif n04 and not n05:
    add_cnt(l,'rst')

  elif n06 and not n07:
    add_cnt(l,'his')

  elif n08 and not n09:
    add_cnt(l,'avg')

  elif n10 and not n11:
    add_cnt(l,'sta')

  else:
    sys.stdout.write(l)
