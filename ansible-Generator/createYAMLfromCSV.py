#Requires Python 3.x 
import csv, sys, argparse

#Argument Processing

helpMsg = '''
This script processes a CSV formated list of EPGs into ansible tasks. This script makes no changes in ACI and is purely for generating ansible yaml files.
'''

argsParse = argparse.ArgumentParser(description=helpMsg)
argsParse.add_argument('-i', '--input-file',  action='store', dest='inputFilePath',  required=True, help='File with CSV Data to be processed into ansible tasks')
argsParse.add_argument('-o', '--output-file', action='store', dest='outputFilePath', required=True, help='Destination File for CSV Data')
args = argsParse.parse_args()

def getTenants(list):
    tenants = []
    for item in list:
        if item['tenant'] not in tenants:
            tenants.append(item['tenant'])
            print(item['tenant'])
    return tenants

def getVrfs(list):
    vrfs = {}
    for line in list:
        if line
    return

def processCSV():
    yaml = open(args.outputFilePath,'w')

    with open(args.inputFilePath, mode='r') as rawFile:
        csvContent = csv.DictReader(rawFile)

        #Generate Tenant List
        tenants = getTenants(csvContent)

        #Generate VRF List
        vrfs = getVrfs(csvContent)

        #TODO Generate unique list of VRF and TENANT combinations 
        #TODO Write Tenant Creation to YAML
        #TODO Write VRF / Tenant creation to YAML
        #TODO Write Bridge Domains to YAML
        #TODO Write EPGs to file.
processCSV()
