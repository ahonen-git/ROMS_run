#!/usr/bin/env bash

casename=v1d
num=001
home_dir=${PWD}
pgm=${home_dir}/oceanM
wdir=/wrk/misumi/roms_cases/$casename
name=${casename}_${num}

rm -f c.$name
rm -f o.$name
rm -f e.$name

if [ ! -d ${wdir} ]
then
    mkdir -p ${wdir}
fi

cp -r External ${wdir}

qsub <<EOF
#PBS -P 151018
#PBS -q xs
#PBS -l select=1:ncpus=2:mem=100mb:mpiprocs=2
#PBS -l walltime=24:00:00
#PBS -N ${name}
#PBS -o o.${name}
#PBS -e e.${name}
#PBS -W umask=022
#PBS -V

cd ${wdir}

mpijob ${pgm} ${home_dir}/${name}.in > ${home_dir}/c.${name}

EOF
