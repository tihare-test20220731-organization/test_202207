#!/bin/bash

python3 setup.py build_sphinx
./docs/sphinx/source/util_bashscript/strip_extra_newline_in_table.bash
