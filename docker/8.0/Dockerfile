# Using the CENTOS container from the docker library
FROM centos:latest

# git and vim are not required but commonly used

# Requirements for Ansible and the ucs sdks
RUN yum install epel-release python3 python3-pip git vim -y && \
pip3 install --upgrade pip

# Install the Ansible and UCS compenents.
RUN pip3 install xmljson lxml ansible pyopenssl jmespath

# jmespath added to support JSON queries.
# pyopenssl used for certificate authentication
# xmljson required for ACI calls
# lxml is for xml processing


