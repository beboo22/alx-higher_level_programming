#!/usr/bin/python3
# test_rectangle.py

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_initWidth(self):
        r = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(r.width, 10)

    def test_initHeight(self):
        r = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(r.height, 20)

    def test_initX(self):
        r = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(r.x, 30)
    
    def test_initY(self):
        r = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(r.y, 40)
    def test_initId(self):
        r = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(r.id, 50)

    def test_width(self):
        r = Rectangle(10, 20)
        r.width = 30
        self.assertEqual(r.width, 30)
        

    def test_width_type_error(self):
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.width = "30"

    def test_width_value_error(self):
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.width = -30

    def test_height(self):
        r = Rectangle(10, 20)
        r.height = 30
        self.assertEqual(r.height, 30)

    def test_height_type_error(self):
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.height = "30"

    def test_height_value_error(self):
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.height = -30

    def test_x(self):
        r = Rectangle(10, 20)
        r.x = 30
        self.assertEqual(r.x, 30)

    def test_x_type_error(self):
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.x = "30"

    def test_x_value_error(self):
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.x = -30

    def test_y(self):
        r = Rectangle(10, 20)
        r.y = 30
        self.assertEqual(r.y, 30)

    def test_y_type_error(self):
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.y = "30"

    def test_y_value_error(self):
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.y = -30

    def test_area(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.area(), 200)

    def test_str(self):
        r = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(str(r), "[Rectangle] (50) 30/40 - 10/20")

    def test_update(self):
        r = Rectangle(10, 20, 30, 40, 50)
        r.update(60, 20, 30, 40, 50)
        self.assertEqual(str(r), "[Rectangle] (60) 40/50 - 20/30")

    def test_to_dictionary(self):
        r = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(r.to_dictionary(), {'id': 50, 'width': 10, 'height': 20, 'x': 30, 'y': 40})

    def test_to_dictionary_update(self):
        r = Rectangle(10, 20, 30, 40, 50)
        r.update(60, 20, 30, 40, 50)
        self.assertEqual(r.to_dictionary(), {'id': 60, 'width': 20, 'height': 30, 'x': 40, 'y': 50})

    def test_multiple_instances(self):
        r1 = Rectangle(10, 20)
        r2 = Rectangle(20, 30)
        self.assertNotEqual(r1.id, r2.id)




if __name__ == '__main__':
    unittest.main()
