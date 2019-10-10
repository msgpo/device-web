#!/bin/bash

SRC=$(dirname "$BASH_SOURCE")
cd $SRC

test -d ~/notebook || cp -R notebook ~
cd ~/notebook

jupyter-lab  -y --no-browser --ip '' --notebook-dir ~/notebook

