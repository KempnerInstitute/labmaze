# Copyright 2019 DeepMind Technologies Limited.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================

"""Install script for setuptools."""

from setuptools import setup, Extension, find_packages
import pybind11
import os

root = os.path.abspath(os.path.dirname(__file__))
base_cc = os.path.join(root, "src", "labmaze", "cc")

# Sources shared by both extensions
core_srcs = [
    os.path.join(base_cc, "algorithm.cc"),
    os.path.join(base_cc, "char_grid.cc"),
    os.path.join(base_cc, "flood_fill.cc"),
    os.path.join(base_cc, "text_maze.cc"),
]

ext_modules = [
    Extension(
        name="labmaze.cc.python._random_maze",
        sources=[
            os.path.join(base_cc, "python", "_random_maze.cc"),
            os.path.join(base_cc, "random_maze.cc"),
            *core_srcs
        ],
        include_dirs=[
            pybind11.get_include(),
            base_cc,
            os.path.join(base_cc, "python"),
            root
        ],
        language="c++",
        extra_compile_args=["/std:c++17"] if os.name == "nt" else ["-std=c++17"],
    ),
    Extension(
        name="labmaze.cc.python._defaults",
        sources=[
            os.path.join(base_cc, "python", "_defaults.cc"),
        ],
        include_dirs=[
            pybind11.get_include(),
            base_cc,
            os.path.join(base_cc, "python"),
            root
        ],
        language="c++",
        extra_compile_args=["/std:c++17"] if os.name == "nt" else ["-std=c++17"],
    ),
]

setup(
    name="labmaze",
    version="1.0.6",
    description="LabMaze: DeepMind Lab’s text maze generator",
    author="DeepMind",
    license="Apache-2.0",
    packages=find_packages(where="src"),
    package_dir={"":"src"},
    ext_modules=ext_modules,
    install_requires=["numpy>=1.8.0", "absl-py"],
    package_data={"labmaze": ["*.png"]},
    zip_safe=False,
    python_requires=">=3.7",
)
