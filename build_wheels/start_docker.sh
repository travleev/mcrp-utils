#!/bin/bash

# list of tags. Note that auditwheel checks if the wheel is eligible fo higher tag and
# thus manylinux1 may not be needed
tags="manylinux2010_x86_64"  # manylinux1_x86_64

# Get updated images 
for plat in "$tags"; do
    echo '*******************************************************************'
    echo $plat;
    image=quay.io/pypa/$plat;
    
    # get the latest image
    docker pull $image;

    # Create the dist folder here, otherwise it will be created within docker with root ownership
    mkdir -p ../dist

    # run build inside the docker image
    docker run --rm -v `pwd`/../:/io $image /io/build_wheels/build_wheels.sh
done