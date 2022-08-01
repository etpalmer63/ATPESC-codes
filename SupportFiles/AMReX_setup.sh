#!/bin/bash

# Source this file to set environment variables for AMReX

# Environment vars for AMReX builds with GNUMake
AMREX_HOME =
AMREX_HYDRO_HOME =

# Add ParaView-5.9 and ffmpeg to path for making visualizations
export PATH = $PATH:/grand/ATPRESC2022/use/MathPackages/ffmpeg
export PATH = $PATH:/grand/ATPRESC2022/use/MathPackages/Paraview/bin
