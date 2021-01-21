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

def getTenants(yaml, csvList):
    # Return only one instance of each tenant name
    tenants = []
    for tenant in csvList:
        if tenant['tenant'] not in tenants:
            tenants.append(tenant['tenant'])
    writeTenants(tenants = tenants, yaml = yaml)
    return

def writeTenants(tenants, yaml):
    #Write YAML to file for each tenant to be created.
    yaml.write('tenants:\n')
    for tenant in tenants:
        yaml.write(f" - Tenant: {tenant}\n")
    return

def getVrfs(csvList, yaml):
    vrf_dict = {}
    for line in csvList:
        if (line['tenant'], line['VRF']) not in vrf_dict or (line['RP'] != 'NA' and line['RP'] != ''):
            vrf_dict[(line['tenant'], line['VRF'])] = line['RP']
    writeVrfs(vrf_dict = vrf_dict, yaml = yaml)
    return


def writeVrfs(vrf_dict, yaml):
    yaml.write('vrfs:\n')
    for item in vrf_dict.items():
        (tenant, vrf), rp = item
        yaml.write(f" - vrf: {vrf}\n")
        yaml.write(f"   tenant: {tenant}\n")

        if rp != 'NA':
            yaml.write(f"   rp: {rp}\n")

def getApps(csvList, yaml):
    app_dict = {}
    for line in csvList:
        if (line['tenant'], line['appProfile']) not in app_dict:
            app_dict[(line['tenant'],line['appProfile'])] = []
    writeApps(yaml=yaml, app_dict=app_dict)
    return

def writeApps(yaml, app_dict):
    yaml.write('aps:\n')
    for item in app_dict:
        (tenant, app) = item
        yaml.write(f' - ap: {app}\n')
        yaml.write(f'   tenant: {tenant}\n')
    return

def processCSV():
    yaml = open(args.outputFilePath,'w')

    with open(args.inputFilePath, mode='r') as rawFile:
        #We open this as a list because we iterate it more than once
        csvContent = list(csv.DictReader(rawFile))

        #Generate Tenant List and write to YAML
        getTenants(yaml = yaml, csvList = csvContent)

        #Generate VRF List and write to YAML
        getVrfs(yaml = yaml, csvList = csvContent)

        #Generate Application Profile List and write to Yaml
        getApps(yaml = yaml, csvList = csvContent)
        
        #TODO Write APs
        #TODO Write Bridge Domains to YAML
        #TODO Write AP to Proper Tenants
        #TODO Write EPGs to file.
processCSV()
