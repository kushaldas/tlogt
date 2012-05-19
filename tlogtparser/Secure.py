import os
import sys
import glob

def get_log_dates():
    """
    Gets the filenames of the secure logs
    """
    names = glob.glob('/var/log/secure*')
    names.sort(reverse=True)
    if '/var/log/secure' == names[-1]:
        names.pop()
        names.insert(0,'/var/log/secure')    
    return names