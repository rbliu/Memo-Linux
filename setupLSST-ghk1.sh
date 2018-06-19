#!/bin/bash

LSSTSW=/export/rliu/lsstsw
. $LSSTSW/bin/setup.sh

echo " "
echo "You are using EUPS:"
which eups
setup lsst_distrib -t b2954
echo " "
echo "############################"
echo "lsst_distrib (v13.0) has been setup!"
echo " _     ____ ____ _____           ____  __  __ "
echo "| |   / ___/ ___|_   _|         |  _ \|  \/  |"
echo "| |   \___ \___ \ | |    _____  | | | | |\/| |"
echo "| |___ ___) |__) || |   |_____| | |_| | |  | |"
echo "|_____|____/____/ |_|           |____/|_|  |_|"

echo "############################"
