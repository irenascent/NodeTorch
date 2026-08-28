# test_nodetorch.py
"""
Tests for NodeTorch module.
"""

import unittest
from nodetorch import NodeTorch

class TestNodeTorch(unittest.TestCase):
    """Test cases for NodeTorch class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodeTorch()
        self.assertIsInstance(instance, NodeTorch)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodeTorch()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
