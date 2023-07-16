#!/usr/bin/python3
# test_base.py
import unittest 
from models.base import Base
class tastBase(unittest.TestCase):
      """Unittests for testing instantiation of the Base class."""

      def test_NoAgr(self):
        b1=Base()
        b2=Base()
        self.assertEqual(b1.id,b2.id-1)
      
      def test_arg(self):
        b1=Base(12)
        self.assertEqual(b1.id,12)
      
      def test_diff_Arg(self):
        b1=Base()
        b2=Base(12)
        b3=Base()
        self.assertEqual(b1.id,b3.id-1)
      
      def test_many_NoArg(self):
        b1=Base()
        b2=Base()
        b3=Base()
        self.assertEqual(b1.id,b3.id-2)
      
      def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)
      
      def test_unique_id(self):
        self.assertEqual(12, Base(12).id)
      
      def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

      def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)
      
      def test_id_max(self):
        max_id = 0
        for i in range(100):
            b = Base()
            if b.id > max_id:
                max_id = b.id
        self.assertNotEqual(max_id, 100)

      def test_id_float(self):
        b = Base(3.14)
        self.assertEqual(b.id, 3.14)

      def test_id_bool(self):
        b1 = Base(True)
        b2 = Base(False)
        self.assertEqual(b1.id, True)
        self.assertEqual(b2.id, False)
      
      def test_id_list(self):
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])

      def test_id_dict(self):
        b = Base({"a": 1, "b": 2})
        self.assertEqual(b.id, {"a": 1, "b": 2})

      def test_id_tuple(self):
        b = Base((1, 2, 3))
        self.assertEqual(b.id, (1, 2, 3))

      def test_id_set(self):
        b = Base({1, 2, 3})
        self.assertEqual(b.id, {1, 2, 3})

      def test_id_complex(self):
        b = Base(3 + 4j)
        self.assertEqual(b.id, 3 + 4j)






if __name__ == '__main__':
    unittest.main()
