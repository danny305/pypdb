import unittest 

## Import from local directory
import sys
sys.path.insert(0, '../pypdb')
from pypdb import *
  
class TestSearchFunctions(unittest.TestCase): 
  
    # Returns True if it successfully connects to the 
    # protein data bank
    def test_querying(self):
    	found_pdbs = Query('actin network').search()     
        self.assertTrue(len(found_pdbs) > 0) 
        self.assertTrue(type(found_pdbs[0]) == str)
        
        # an error page would be a longer string
        self.assertTrue(len(found_pdbs[0]) < 10)

  
if __name__ == '__main__': 
    unittest.main() 