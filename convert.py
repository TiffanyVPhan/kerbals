#!/usr/bin/python3
import pandas as pd
import json
import sys
import math

def xml_obj(dict):
    string = ""
    for key in dict.keys():
        string += '    <{}>{}</{}>\n'.format(key, dict[key], key)
    return string
    
def transform(val):
    return (100*math.atan(val) + 50*math.pi) / math.pi

kerbals = pd.read_csv('kerbals.csv', delimiter=',')

kerbals['Courage'] = kerbals['Courage'].apply(transform)
kerbals['Stupidity'] = kerbals['Stupidity'].apply(transform)

kerbals_dict = kerbals.to_dict(orient='record')

if len(sys.argv) < 2: 
     print('Not enough arguments.')
     exit(1)

elif len(sys.argv) > 3: 
     print("Too many arguments.")
     exit(1)

if sys.argv[1] == 'json':
    kerbals_json = json.dumps(kerbals_dict, indent = 4)
    print(kerbals_json)
    if sys.argv[2] == '-f':
        with open('kerbals.json', 'w') as f:
            json.dump(kerbals_dict, f, indent = 4)
    else:
        print("\nInvalid flag: {}".format(sys.argv[2]))
 
elif sys.argv[1] == 'xml':
    xml = ""
    xml += '<?xml version="1.0" encoding="UTF-8"?>\n<Kerbals>\n'
    for i in range(len(kerbals_dict)):
        xml += '  <Kerbal>\n' + xml_obj(kerbals_dict[i]) + '  </Kerbal>\n'
    xml += '</Kerbals>'
    print(xml)

    if sys.argv[2] == '-f':
        file = open('kerbals.xml', 'w')
        file.write(xml)
    else:
        print("\nInvalid flag: {}".format(sys.argv[2]))

else:
    print('\nInvalid Arguments: {}'.format(sys.argv))