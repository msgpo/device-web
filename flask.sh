#!/bin/bash

SRC=$(dirname "$BASH_SOURCE")
cd $SRC

export FLASK_APP=app.py
flask run
