#!/bin/bash

# list of tags. Note that auditwheel checks if the wheel is eligible fo higher tag and
# thus manylinux1 may not be needed
tags="manylinux2010_x86_64"  # manylinux1_x86_64

# Specifyfolder containing package to build
pack="$1"
cdir=`pwd`
for plat in "$tags"; do
    echo '*******************************************************************'
    echo $plat;
    image=quay.io/pypa/$plat;
    
    # get the latest image
    # docker pull $image;

    cd "$pack"
    # Create the dist folder here, otherwise it will be created within docker with root ownership
    mkdir -p dock-dist1
    mkdir -p dock-dist2

    # run build inside the docker image
    docker run --rm -e PLAT=$plat -v `pwd`:/_pack -v "$cdir":/_build_wheels $image /_build_wheels/build_wheels.sh
done
