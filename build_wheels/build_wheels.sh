#!/bin/bash 

# Taken from https://github.com/pypa/python-manylinux-demo/blob/master/travis/build-wheels.sh
# THe script should be started from docker images, see start_docker.sh


# Compile wheels. 
# Here is assumed that pythons in the docker image are installed to
# /opt/python/cp* and the package directory containing setup.py and
# dev-requirements.txt is mounted to /io.
cd /io

# Unique folder to place generated whell
dd=`mktemp -d -p . dist-XXX`

for PYBIN in /opt/python/cp27*/bin; do
    "${PYBIN}/pip" install -r dev-requirements.txt
    "${PYBIN}/python" setup.py bdist_wheel --dist-dir $dd
done

# Bundle external shared libraries into the wheels generated at the previus step
# and place results to common dist/
for whl in $dd/mcrp_splitters*-linux_x86_64.whl; do
    auditwheel repair "$whl"  -w dist
done

