#!/usr/bin/env bash

source build.config

num=${R_NUM}
name=${CASE_NAME}_${num}

if [ -e ${PGM} ]; then
  cp ${PGM} ${WORK_DIR}/bin/${PGM}
else
  echo "Error: no ${PGM} exists."
  echo 
  exit 0
fi
cp -r External ${WORK_DIR}

qsub <<EOF
#PBS -P ${D_CODE}
#PBS -q ${QUE}
#PBS -l select=${N_NODES}:ncpus=${N_CPUS}:mem=100mb:mpiprocs=${N_MPIP}
#PBS -l walltime=${WALL_TIME}
#PBS -N ${JOB_NAME}
#PBS -o ${WORK_DIR}/log/o.${name}
#PBS -e ${WORK_DIR}/log/e.${name}
#PBS -W umask=022
#PBS -V

cd ${WORK_DIR}

mpijob ${WORK_DIR}/bin/${PGM} ${HOME_DIR}/${name}.in > ${WORK_DIR}/log/c.${name}

cp ${HOME_DIR}/${name}.in ${WORK_DIR}/in
mv ${WORK_DIR}/*.nc       ${WORK_DIR}/out

EOF
