import unittest
import sys

# Add the parent directory to the path so that we can import the module to be tested
sys.path.append('../')

from load_file import read_noverlap_results

class TestReadNoverlapResults(unittest.TestCase):
    def test_read_noverlap_results(self):
        """Tests that the read_noverlap_results function returns the correct list."""
        
        # Call the function to be tested
        result_list = read_noverlap_results('test_sequence.txt')
        expected_result = ['ggtctatcaccct', 
                           'atcaccctattaa', 
                           'tattaaccactca', 
                           'accactcacggga', 
                           'ctcacgggagctc', 
                           'gagctctccatgc', 
                           'tccatgcatttgg']
        
        # Check that the result_list is the same as the expected_result
        self.assertEqual(result_list, expected_result)

if __name__ == '__main__':
    unittest.main()



