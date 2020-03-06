#!/bin/bash 

# Taken from https://github.com/pypa/python-manylinux-demo/blob/master/travis/build-wheels.sh
# THe script should be started from docker images, see start_docker.sh


# Compile wheels. 
# Here is assumed that pythons in the docker image are installed to
# /opt/python/cp* and the package directory containing setup.py and
# dev-requirements.txt is mounted to /_pack (see start_docker.sh).
cd /_pack

# Unique folder to place generated whell
dd1=`mktemp -d -p . dock-dist1-XXX`
# dd2=`mktemp -d -p . dock-dist2-XXX`

for PYBIN in /opt/python/cp27*/bin; do
    "${PYBIN}/pip" install -r dev-requirements.txt

    # The build wheels commands below might use previously existing build and dist
    # folders.Ensure they are not available:
    rm -rf build/ dist/
    "${PYBIN}/pip" wheel . -w $dd1 --no-deps

    # rm -rf build/ dist/
    # "${PYBIN}/python" setup.py bdist_wheel --dist-dir $dd2 
done

# Bundle external shared libraries into the wheels generated at the previus
# step and place results to common dist/
for whl in $dd1/*.whl; do
    auditwheel repair "$whl"  --plat $PLAT -w dock-dist1
done

# for whl in $dd2/*.whl; do
#     auditwheel repair "$whl"  --plat $PLAT -w dock-dist2
# done
