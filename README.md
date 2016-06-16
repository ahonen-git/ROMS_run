# ROMS_run

ROMS_run provides scripts required for running ROMS.

This master branch is to run the model in inx.

## Requirements
- gnu-sed (homebrew)
- libmpc (homebrew)
- hdf5 (self compile)
- zlib (self compile)
- netcdf (self compile)
- netcdf-fortran (self compile)

## Procedure to run ROMS

### 1. Configure ROMS
- Edit build.config.
- Edit ${CASE_NAME}.h to set cpp flags.

### 2. Build ROMS
- Build ROMS
        ``` sh
        $ ./build.bash -j 8
        ```

### 3. Run ROMS
- Edit **go.sh** and set **$num**.
- Edit **${CASE_NAME}_${num}.in** to set configuration for this run.
- Run ROMS
        ```sh
        $ ./go.sh
        ```

## Secs in typical time periods for 365.25 days in a year

|Period|Secs    |
|------|--------|
|1 sec |1       |
|1 day |86400   |
|1 mon |2629800 |
|1 yr  |31557600|
