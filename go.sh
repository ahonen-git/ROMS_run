#!/usr/bin/env bash

source build.config

num=${R_NUM}
name=${CASE_NAME}_${num}

cp ${PGM} ${WORK_DIR}/bin/${PGM}
cp -r External ${WORK_DIR}

qsub <<EOF
#PBS -P ${D_CODE}
#PBS -q ${QUE}
#PBS -l select=${N_NODES}:ncpus=${N_CPUS}:mem=100mb:mpiprocs=${N_MPIP}
#PBS -l walltime=${WALL_TIME}
#PBS -N ${JOB_NAME}
#PBS -o o.${name}
#PBS -e e.${name}
#PBS -W umask=022
#PBS -V

cd ${WORK_DIR}

mpijob ${WORK_DIR}/bin/${PGM} ${HOME_DIR}/${name}.in > ${HOME_DIR}/c.${name}

mv ${HOME_DIR}/c.${name}  ${WORK_DIR}/log/c.${name}
mv ${HOME_DIR}/e.${name}  ${WORK_DIR}/log/e.${name}
mv ${HOME_DIR}/o.${name}  ${WORK_DIR}/log/o.${name}
cp ${HOME_DIR}/${name}.in ${WORK_DIR}/in/${name}.in
mv ${WORK_DIR}/*.nc       ${WORK_DIR}/out/

EOF
