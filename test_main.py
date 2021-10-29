#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 16:09:06 2021

@author: hero
"""

import unittest
from unittest import TestCase
from main import add, subtract, multiply

class TestSecureCX(TestCase):
     
    def test_add(self):
        self.assertEqual(add(2,3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(2,3), -1)

    def test_multiply(self):
        self.assertEqual(multiply(2,3), 6)
if __name__ == '__main__':
    unittest.main()