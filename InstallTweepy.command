#!/bin/bash


BASEDIR="$( dirname "$0" )"
cd "$BASEDIR"/InstallData/tweepy-master

sudo python setup.py install
