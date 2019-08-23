#!/bin/bash

[ -d ~/workspace ] || mkdir ~/workspace
cd ~/workspace

jupyter-lab  -y --no-browser --allow-root --ip '' --notebook-dir ~/workspace
