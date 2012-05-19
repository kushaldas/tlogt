import unittest
from pprint import pprint

class SecureSudoTest(unittest.TestCase):
    """
    To test secure log details
    """
    def runTest(self):
        from tlogtparser import Secure
        data = Secure.get_log('testdata/secure')
        assert data[97]['status'] == 'warning'
        assert data[99]['status'] == 'error'
        
        
if __name__ == '__main__':
    unittest.main()