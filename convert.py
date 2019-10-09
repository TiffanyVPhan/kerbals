#!/usr/bin/python3
import json
import sys
import math

# Helper Functions
def xml_obj(dict):
    """Concatenate each key value pair for one Kerbal dictionary in XML syntax."""
    string = ""
    for key in dict.keys():
        string += '    <{}>{}</{}>\n'.format(key, dict[key], key)
    return string
    
def transform(val):
    """Calculate the true values of `val` in percentages."""
    return (100*math.atan(val) + 50*math.pi) / math.pi

kerbals = []
with open('kerbals.csv') as f:
    keys = f.readline().strip().split(',')
    keys = [i.replace('"','') for i in keys]
    for line in f:
        mydict = {}
        for index, val in enumerate(line.strip().split(',')):
            if keys[index] == 'FirstName' or keys[index] == 'LastName' or keys[index] == 'Job':
                mydict[keys[index]] = val.replace('"', '')
            else:
                # Transforming Courage and Stupidity columns to percentages.
                if keys[index] == 'Courage' or keys[index] == 'Stupidity':
                    mydict[keys[index]] = transform(float(val))
                else:
                    mydict[keys[index]] = int(val)
        kerbals.append(mydict)

# User input error checking
if len(sys.argv) < 2:
     print('Not enough arguments.')
     exit(1)

elif len(sys.argv) > 3: 
     print("Too many arguments.")
     exit(1)

# JSON
if sys.argv[1] == 'json':

    # Converting dictionary to JSON array
    print(json.dumps(kerbals))

    # Writing JSON array to file
    if len(sys.argv) == 3:
        if sys.argv[2] == '-f':
            with open('kerbals.json', 'w') as f:
                json.dump(kerbals, f, indent = 4)
        else:
            print("\nInvalid flag: {}".format(sys.argv[2]))
 

 # XML
elif sys.argv[1] == 'xml':
    xml = ""
    xml += '<?xml version="1.0" encoding="UTF-8"?>\n<Kerbals>\n'
    for i in range(len(kerbals)):
        xml += '  <Kerbal>\n' + xml_obj(kerbals[i]) + '  </Kerbal>\n'
    xml += '</Kerbals>'
    print(xml)

    # Writing XML array to file
    if len(sys.argv) == 3:
        if sys.argv[2] == '-f':
            file = open('kerbals.xml', 'w')
            file.write(xml)
        else:
            print("\nInvalid flag: {}".format(sys.argv[2]))

# User input Error Checking
else:
    print('\nInvalid Arguments: {}'.format(sys.argv))