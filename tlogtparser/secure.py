import os
import sys
import glob
from pprint import pprint

def get_log_dates():
    """
    Gets the filenames of the secure logs
    """
    #Find all required file names
    names = glob.glob('/var/log/secure*')
    names.sort(reverse=True)
    #Remove /var/log/messages from the end and
    # add it in the front
    if '/var/log/secure' == names[-1]:
        names.pop()
        names.insert(0,'/var/log/secure')    
    return names


def get_log(path='/var/log/secure'):
    """
    Get the log details
    """
    #Check if the file exists
    if not os.path.isfile(path):
        return {'error': 'File not found'}
    lines = None
    with open(path) as fobj:
        lines = [find_extract(line) for line in fobj]
    return lines
        
def find_extract(line=''):
    """
    Parses the line
    """
    #For now I will use raw parsing
    tokens = line.split(' ')
    if len(tokens) >= 5:
        #print tokens[4]
        if tokens[4] == 'sudo:':
            if line.find('incorrect password attempt') != -1:
                return {'text': line, 'status': 'error'}
            else:
                return {'text': line, 'status': 'warning'}
        else:
            return {'text': line, 'status': 'info'}