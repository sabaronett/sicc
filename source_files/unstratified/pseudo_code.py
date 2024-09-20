#!/usr/bin/env python3
#==============================================================================
# athena_opac.py
#
# Creates multifrequency opacity tables for input into Athena++.
#
# This script takes as input (1) a RADMC-3D-formatted opacity table with the
# filename structure `dustkappa_*.inp` (see https://www.ita.uni-heidelberg.de/
# ~dullemond/software/radmc-3d/manual_radmc3d/
# inputoutputfiles.html#the-dustkappa-inp-files); (2) an Athena++-formatted
# input file with the following requred parameters:
#   <radiation>
#   n_frequency      # no. of frequency groups
#   frequency_min    # [0, \nu_min) [k_BT_0/h] < 0 < [Hz]
#   frequency_max    (if n_frequency > 2) # [\nu_max, \inf)
#
#   <problem>
#   n_temperature    # no. of temperature groups
#   temperature_min  # min mean opacity temperature [K]
#   temperature_max  # max mean opacity temperature [K]
#
# Author: Stanley A. Baronett
# Created: 2024-04-19
# Updated: 2024-08-20
#==============================================================================
import numpy as np
from pathlib import Path
from radmc3dPy import analyze
from radmc3dPy.natconst import *
from scipy import integrate
from scipy.constants import c, h, k
import sys
sys.path.insert(0,'/home/stanley/github/PrincetonUniversity/athena/vis/python')
import athena_read
import warnings