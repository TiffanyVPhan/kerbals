#!/usr/bin/python3
import pandas as pd
import json
import sys
import math

def xml_obj(dict):
    for key in dict.keys():
        print('    <{}>'.format(key), end="")
        print(dict[key], end="")
        print('</{}>'.format(format(key)))
    
def transform(val):
    return (100*math.atan(val) + 50*math.pi) / math.pi

kerbals = pd.read_csv('kerbals.csv', delimiter=',')

kerbals['Courage'] = kerbals['Courage'].apply(transform)
kerbals['Stupidity'] = kerbals['Stupidity'].apply(transform)

kerbals_dict = kerbals.to_dict(orient='record')

if sys.argv[1] == 'json':
    kerbals_json = json.dumps(kerbals_dict, indent = 4)
    print(kerbals_json)

elif sys.argv[1] == 'xml':
    print('<?xml version="1.0" encoding="UTF-8"?>\n<Kerbals>')
    for i in range(len(kerbals_dict)):
        print('  <Kerbal>')
        xml_obj(kerbals_dict[i])
        print('  </Kerbal>')
    print('</Kerbals>')