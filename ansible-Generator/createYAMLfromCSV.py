#Requires Python 3.x 
import csv, sys, argparse, collections

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
    return tenants

def getVrfs(csvList):
    vrfs = []
    for line in csvList:
        addLine = True
        for oneVRF in vrfs:
            if line['tenant'] == oneVRF['tenant'] and line['VRF'] == oneVRF['VRF']:
               addLine = False
        if addLine == True:
           vrfs.append({'tenant': line['tenant'], 'VRF': line['VRF'], 'RP': line['RP']})
    return vrfs

def writeTenants(tenants, yaml):
    yaml.write('tenants:\n')
    for tenant in tenants:
        yaml.write(f" - Tenant: {tenant}\n")
    return

def writeVrfs(vrfs, yaml):
    yaml.write('vrfs:\n')
    for vrf in vrfs:
        yaml.write(f" - vrf: {vrf['VRF']}\n")
        yaml.write(f"   tenant: {vrf['tenant']}\n")

        #If the RP field is blank or equal to NA, we don't need this field
        if vrf['RP'] != '' and vrf['RP'] != 'NA':
            yaml.write(f"   rp: {vrf['RP']}\n")
    return

def processCSV():
    yaml = open(args.outputFilePath,'w')

    with open(args.inputFilePath, mode='r') as rawFile:
        #We open this as a list because we iterate it more than once
        csvContent = list(csv.DictReader(rawFile))

        #Generate Tenant List
        tenants = getTenants(csvContent)

        #Generate VRF List
        vrfs = getVrfs(csvContent)

        #Write out data for various elements.
        writeTenants(tenants=tenants, yaml=yaml)
        writeVrfs(vrfs=vrfs, yaml=yaml)
        #TODO Write VRF / Tenant creation to YAML
        #TODO Write Bridge Domains to YAML
        #TODO Write AP to Proper Tenants
        #TODO Write EPGs to file.
processCSV()
