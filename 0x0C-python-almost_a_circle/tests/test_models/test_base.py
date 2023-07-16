#!/usr/bin/python3
# test_base.py
import unittest 
from models.base import Base
class tastBase(unittest.TestCase):
      def test_NoAgr(self):
        b1=Base()
        b2=Base()
        self.assertEqual(b1.id,b2.id-1)
if __name__ == '__main__':
    unittest.main()
