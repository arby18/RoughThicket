# test_roughthicket.py
"""
Tests for RoughThicket module.
"""

import unittest
from roughthicket import RoughThicket

class TestRoughThicket(unittest.TestCase):
    """Test cases for RoughThicket class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RoughThicket()
        self.assertIsInstance(instance, RoughThicket)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RoughThicket()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
