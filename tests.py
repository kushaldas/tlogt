import unittest
from pprint import pprint

class SecureSudoTest(unittest.TestCase):
    """
    To test Secure log details
    """
    def runTest(self):
        from tlogtparser import secure
        data = secure.get_log('testdata/secure')
        assert data[97]['status'] == 'warning'
        assert data[99]['status'] == 'error'
        
class BootTest(unittest.TestCase):
	"""
	To test basic Boot details
	"""
	def runTest(self):
		from tlogtparser import boot
		data = boot.get_log('testdata/boot')
		assert data[116]['status'] == 'error'
		assert data[117]['status'] == 'info'
        
        
if __name__ == '__main__':
    unittest.main()
    
