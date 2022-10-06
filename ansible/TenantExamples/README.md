# Ansible Examples with Centralized Variables

This area demonstrates simple methods of creating VRFs, bridge domains and EPGs with more centralized variables. This is a demonstration of a methodology more than a recommended method of deployment. There are many ways you an populate the variables, and I didn't attempt to set every possible setting through variables. 

## Prerequisites
This script was tested with:
- Ansible 2.10.17
- cisco.aci Version 2.2.0 from from Ansible Galaxy 
- A private and corresponding public x509 certificate file associated with an ACI user
- Cisco ACI version 5.2

## Running this demo example
To run this demo, edit the inventory-public.ini file to associate your user authentication and APIC IP address. The run the following command from the same directory as the playbook. 

```
ansible-playbook -i inventory-public.ini playbook-ACI-Tenant-VRF-BD-EGP.demo.yaml
```

