# Copyright 2020 Lawrence Livermore National Security, LLC and other CLIPPy Project Developers.
# See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: MIT

# command prefix used to specify clippy task management with the HPC cluster
# for instance, if using slurm this could be set to 'srun -n1 -ppdebug'
cmd_prefix = ''

# contol the log level of clippy
loglevel = 0

# PRIVATE: this dict contains the class types that clippy has constructed.
#          once constructed clippy will get the definition from this dict
#          to create new instances.
_dynamic_types = {}
