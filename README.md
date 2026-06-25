# fahdaptive
A set of scripts to be used for running adaptive-sampling type simulations on distributed platforms like folding@home

## Setup

To replicate the environment used in previous efforts, use `environment.yml`. Generally\
 this library requires `pyEmma` and `openmm>=7.7`.

NOTE: There are two considerations you must make when using this implementation:
1. You will need to save all the atoms (including solvent) for each frame (these frames are how new seeds are generated).
2. You need a `top.pdb` structure file that has _all_ the atoms of the MD simulations run.

## Running HPC scripts

The scripts and platform is intended to run on two machines. The scripts in `hpc-scripts`\
 must be run on an HPC sytem on the whole dataset (and ports it over on the work-server). \
Inside `hpc-scripts/adaptive-msm-*.py` scripts you can specify project-ID, number of \
 CLONEs (and number of seeds), and number of cores for parallelizing (`n_cores`).

## Running WS scripts

The scripts inside `ws-scripts` are meant to be placed inside the relevant `project`\
 directories. In `ws-scripts/sample-project.xml` is a sample `project.xml` that\
 utilizes a `SEEDS` directory (copied over by `hpc-scripts/adaptive-msm-*.py`) that\
 and runs `ws-scripts/next-state.py` inside the FAH-work process to launch the\
 next seeds.

A sample `core.xml` is also included.

## Analysis

You can also visualize the progress of each seeds by extracting each seeds using\
 `seed-analysis/extract-seeds-*.py`. The example provided here runs `extract-seeds`\
 and also generates a plot by extracting features from each seeds (2 distances).\
 This can be modified but will run continuously.

