#!/usr/bin/python3
"""
Goal:
- perform a dig against a hostname
- parse the A records from the dig
- print A records to screen
- number of records
"""
import subprocess
def get_a_record(hostname):
    """
    this function will call dig and obtain the A records from a given hostname
    """
    dig = subprocess.run(['dig', hostname], stdout=subprocess.PIPE)
    return dig.stdout

def parse_out(data):
    """
    this function will clean up the output of the A record
    - convert bytes to string
    - slise at newlines
    - cleaner digoutput    
    """
    print(type(data))
    print(type(data.decode('utf-8')))
    data = data.decode('utf-8')
    new_data = data.split('\n')   
    for index,line in enumerate(new_data):
        print(index,line)
    a_record = new_data[13].split('\t')
    return a_record[-1]

def print_output(data):
    print('The IP Address of Google is {}'.format(data))

g = get_a_record('google.com')
parsed = parse_out(g)
print_output(parsed)
