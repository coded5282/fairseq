#!/bin/sh
pip install -e .
export MKL_THREADING_LAYER=GNU
cd examples/MMPT
pip install -e .
pip install -r requirements.txt
