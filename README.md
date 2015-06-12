# ROMS_run

ROMS_run provides scripts required for running ROMS.

## Procedure to run ROMS
1. Edit go_001.sh
[ go_001.sh ]
``` sh
casename=test
num=001
home_dir=${PWD}
pgm=${home_dir}/oceanM
wdir=/wrk/misumi/roms_cases/$casename
name=${casename}_${num}
```
