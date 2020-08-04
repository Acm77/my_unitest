#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import re
import unittest
import my_unitest
from my_unitest.my_test_style import MyTestRunner


class ExecTest(object):

    @staticmethod
    def _get_test_cls_obj():
        test_cls_list = []
        rule = re.compile('[A-Z].*$')
        for attr_name in dir(my_unitest):
            if rule.match(attr_name) and getattr(my_unitest, attr_name, None):
                test_cls_list.append(getattr(my_unitest, attr_name, None))
        return test_cls_list

    @staticmethod
    def _get_test_func_name(cls_obj):
        test_func_list = []
        for func_name in dir(cls_obj):
            if func_name.startswith('test_'):
                test_func_list.append(cls_obj(func_name))
        return test_func_list

    @classmethod
    def run(cls):
        suite = unittest.TestSuite()

        test_cls_list = cls._get_test_cls_obj()
        for test_cls in test_cls_list:
            suite.addTests(cls._get_test_func_name(test_cls))

        runner = MyTestRunner()
        runner.run(suite)


if __name__ == "__main__":
    ExecTest.run()
