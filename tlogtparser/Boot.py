import os
import sys
import glob

def get_log_dates():
    """
    Fetch the boot log files sequentially
    """
    names = glob.glob('/var/log/boot*')
    names.sort(reverse=True)
    if '/var/log/boot' == names[-1]:
        names.pop()
        names.insert(0,'/var/log/boot')    
    return names
    
def get_log(path='/var/log/boot.log'):
    """
    Gets the log details from the boot log
    """
    #Check file existence
    if not os.path.isfile(path):
        return {'error': 'File not found'}
    lines = None
    with open(path) as fobj:
        lines = [get_result(line) for line in fobj]
    return lines

def get_result(line=''):
    """
    Parses the file
    """
    if line.find('failed') !=-1 or line.find('Failed') !=-1:
        line=line.strip()
        return {'text': line, 'status': 'error'}
    else:
        return {'text': line, 'status': 'info'}
                    
