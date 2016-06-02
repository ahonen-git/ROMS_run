# ROMS_run

ROMS_run provides scripts required for running ROMS.

This master branch is to run the model in inx.

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
