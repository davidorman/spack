##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class PyMaestrowf(PythonPackage):
    """A general purpose workflow conductor for running multi-step
       simulation studies."""

    homepage = "https://github.com/LLNL/maestrowf/"
    url      = "https://github.com/LLNL/maestrowf/archive/v1.1.2.tar.gz"

    version('1.1.2', 'a9e05d82910cd2dd077321fb9b0c8dcd')
    version('1.1.1', 'd38bbf634de4f29fd01d1864ba2f70e0')
    version('1.1.0', '3c20bf36fbb85d14c3bfdb865944a409')
    version('1.0.1', '6838fc8bdc7ca0c1adbb6a0333f005b4')

    depends_on('py-setuptools', type='build')
    depends_on('py-pyyaml',     type=('build', 'run'))
    depends_on('py-six',        type=('build', 'run'))
    depends_on('py-enum34',     type=('build', 'run'))
    depends_on('py-tabulate',   type=('build', 'run'), when='@1.1.0:')
    depends_on('py-filelock',   type=('build', 'run'), when='@1.1.0:')
