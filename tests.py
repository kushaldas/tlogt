import unittest
from pprint import pprint

class SecureGetLogTest(unittest.TestCase):
    """
    To test secure log details
    """
    def runTest(self):
        from tlogtparser import Secure
        data = Secure.get_log('testdata/secure')
        for datum in data:
            pprint(datum)
        
if __name__ == '__main__':
    unittest.main()