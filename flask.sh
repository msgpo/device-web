#!/bin/bash

SRC=$(dirname "$BASH_SOURCE")
cd $SRC

IP=$(ip address show wlan0 | sed -ne 's/^[ \t]*inet[ \t]*\([0-9.]\+\)\/.*$/\1/p')

export FLASK_APP=app.py
flask run -h ${IP}
