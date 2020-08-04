#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

import unittest
from common.utils import sort_data
from my_unitest.my_test_style import MyTestRunner
from my_unitest.base_test_case import BaseTestCase


sort_list = [
    {'desc': 'i am 4', 'sort': 4},
    {'desc': 'i am 1', 'sort': 1},
    {'desc': 'i am 2', 'sort': 2},
    {'desc': 'i am 3', 'sort': 3},
]


class TestSortData(BaseTestCase):
    def test_reverse_true(self):
        self.assertEqual(sort_data(sort_list, 'sort', reverse=True),
                         [{'sort': 4, 'desc': 'i am 4'},
                          {'sort': 3, 'desc': 'i am 3'},
                          {'sort': 2, 'desc': 'i am 2'},
                          {'sort': 1, 'desc': 'i am 1'}]
                         )

    def test_reverse_false(self):
        self.assertEqual(sort_data(sort_list, 'sort', reverse=False),
                         [{'sort': 1, 'desc': 'i am 1'},
                          {'sort': 2, 'desc': 'i am 2'},
                          {'sort': 3, 'desc': 'i am 3'},
                          {'sort': 4, 'desc': 'i am 4'}]
                         )

    def test_memory_addr(self):
        self.assertNotEqual(id(sort_data(sort_list, 'sort')), id(sort_list))

    def test_sort_key_not_exist(self):
        diy_sort_list = [
            {'desc': 'i am 4', 'sort': 4},
            {'desc': 'i am 1', 'sort': 1},
            {'desc': 'i am 5'},
            {'desc': 'i am 2', 'sort': 2},
            {'desc': 'i am 3', 'sort': 3},
        ]
        self.assertEqual(sort_data(diy_sort_list, 'sort'), diy_sort_list)


if __name__ == '__main__':
    unittest.main(testRunner=MyTestRunner())
