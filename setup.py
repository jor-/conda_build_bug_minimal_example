# Copyright (C) 2011-2018 Joscha Reimer jor@informatik.uni-kiel.de
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""A setuptools based setup module.
https://packaging.python.org/en/latest/distributing.html
"""

import setuptools
import os.path


# Setup
setuptools.setup(
    # general informations
    name='bug_example',
    description='measurements functions',

    author='Joscha Reimer',
    author_email='jor@informatik.uni-kiel.de',
    license='AGPLv3+',

    # version
    version='1.0',

    # packages to install
    packages=setuptools.find_packages(),

    # dependencies
    python_requires='>=3.2',
    setup_requires=[
        'setuptools>=0.8',
        'pip>=1.4',
    ],
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'overrides',
        'matrix-decomposition',
    ],
)
