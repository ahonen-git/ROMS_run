# ROMS_run

ROMS_run provides scripts required for running ROMS.

## Procedure to run ROMS
### 1. Edit go_001.sh

[ go_001.sh ]
``` sh
casename=v1d
num=001
home_dir=${PWD}
pgm=${home_dir}/oceanM
wdir=/wrk/misumi/roms_cases/$casename
name=${casename}_${num}
```
- Edit casename.
- Note that wdir is created in /wrk/misumi/roms_cases/$casename
- casename is also used in **in-file name**. 

### 2. Edit v1d_001.in

[ v1d_001.in ]
``` sh
VARNAME = External/varinfo.dat
...
GRDNAME == /wrk/misumi/roms_data/v1d/v1d_grd.nc
ININAME == /wrk/misumi/roms_data/v1d/v1d_ini.nc
...
FRCNAME == /wrk/misumi/roms_data/v1d/v1d_frc.nc   \
           /wrk/misumi/roms_data/v1d/v1d_sflux.nc

...
GSTNAME == ocean_gst.nc
RSTNAME == v1d_rst001.nc
HISNAME == v1d_his001.nc
TLMNAME == ocean_tlm.nc
TLFNAME == ocean_tlf.nc
ADJNAME == ocean_adj.nc
AVGNAME == v1d_avg001.nc
DIANAME == ocean_dia.nc
STANAME == ocean_sta.nc
FLTNAME == ocean_flt.nc
...
BPARNAM =  External/bec.in
...
```

### 3. Copy binary

``` sh
% cp ../ROMS_build/oceanM .
```
