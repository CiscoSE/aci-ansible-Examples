# Using the CENTOS container from the docker library
FROM centos:latest

# git and vim are not required but commonly used

# Requirements for Ansible and the ACI sdks
RUN dnf install python38 python38-pip git vim -y && \
pip3 install --upgrade pip

# Install the Ansible and UCS compenents.
RUN pip3 install xmljson lxml ansible pyopenssl jmespath

# jmespath added to support JSON queries.
# pyopenssl used for certificate authentication
# xmljson required for ACI calls
# lxml is for xml processing

# We must update last in order to ensure that we get ansible
# mapped to python 3.8. Otherwise the update installs 3.6
# and we end up with ansible running the wrong version. 
RUN dnf update -y
