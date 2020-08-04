#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

import unittest
from common.utils import get_cls_attr_values
from my_unitest.my_test_style import MyTestRunner
from my_unitest.base_test_case import BaseTestCase


class A(object):
    class Status(object):
        z = 1
        y = 2
        x = 3
        w = '!'
        v = 'world'
        u = 'hello'

        def t(self):
            pass


class TestGetClsAttrValues(BaseTestCase):
    def test_int_value(self):
        attr_values = get_cls_attr_values(A.Status)
        self.assertEqual(attr_values, [3, 2, 1])

    def test_str_value(self):
        attr_values = get_cls_attr_values(A.Status, type_obj=str)
        self.assertEqual(attr_values, ['hello', 'world', '!'])


if __name__ == '__main__':
    unittest.main(testRunner=MyTestRunner())
