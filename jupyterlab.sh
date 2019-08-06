#!/bin/bash

[ -d ~/workspace ] || mkdir ~/workspace

# IP=$(ip address | sed -ne '/127.0.0.1/!{s/^[ \t]*inet[ \t]*\([0-9.]\+\)\/.*$/\1/p}')
# IP=127.0.0.1
IP=$(ip address show wlan0 | sed -ne 's/^[ \t]*inet[ \t]*\([0-9.]\+\)\/.*$/\1/p')

jupyter-lab  -y --no-browser --allow-root --ip ${IP} --notebook-dir ~/workspace
