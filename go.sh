#!/usr/bin/env bash

function q0_submit(){
qsub <<EOF
#PBS -P ${D_CODE}
#PBS -q ${QUE}
#PBS -l select=${N_NODES}:ncpus=${N_CPUS}:mem=100mb:mpiprocs=${N_MPIP}
#PBS -l walltime=${WALL_TIME}
#PBS -N ${JOB_NAME}_${R_NUM}
#PBS -o ${WORK_DIR}/log/o.${name}
#PBS -e ${WORK_DIR}/log/e.${name}
#PBS -W umask=022
#PBS -V

cd ${WORK_DIR}

mpijob ${WORK_DIR}/bin/${PGM} ${HOME_DIR}/${name}.in > ${WORK_DIR}/log/c.${name}

cp ${HOME_DIR}/${name}.in ${WORK_DIR}/in
mv ${WORK_DIR}/*.nc       ${WORK_DIR}/out

EOF
}

function q1_submit(){
qsub <<EOF
#PBS -P ${D_CODE}
#PBS -q ${QUE}
#PBS -l select=${N_NODES}:ncpus=${N_CPUS}:mem=100mb:mpiprocs=${N_MPIP}
#PBS -l walltime=${WALL_TIME}
#PBS -N ${JOB_NAME}_${R_NUM}
#PBS -o ${WORK_DIR}/log/o.${name}
#PBS -e ${WORK_DIR}/log/e.${name}
#PBS -W umask=022
#PBS -W depend=afterok:${P_JOB}
#PBS -V

cd ${WORK_DIR}

mpijob ${WORK_DIR}/bin/${PGM} ${HOME_DIR}/${name}.in > ${WORK_DIR}/log/c.${name}

cp ${HOME_DIR}/${name}.in ${WORK_DIR}/in
mv ${WORK_DIR}/*.nc       ${WORK_DIR}/out

EOF
}


source build.config

num=${R_NUM}
name=${CASE_NAME}_${num}

if [ ${P_JOB:-UNDEF} = "UNDEF" ]; then
  if [ -e ${PGM} ]; then
    cp ${PGM} ${WORK_DIR}/bin/${PGM}
  else
    echo "Error: no ${PGM} exists."
    echo 
    exit 0
  fi
  cp -r External ${WORK_DIR}

  q0_submit
else
  q1_submit
fi
