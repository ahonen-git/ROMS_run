#!/usr/local/bin/python

import sys

argvs = sys.argv
argc = len(argvs)

if (argc != 2):
  print 'Usage: python %s go_XXX.csh ' % argvs[0]
  quit()

f0 = open(argvs[1])

for l in f0:
  n = l.find('set no')

  if n != -1:
    x = l.split('=')
    cnt = int(x[1])
    cnt = cnt + 1
    print "set no = " + "{0:0>3}".format(cnt)

  if n == -1:
    sys.stdout.write(l)
