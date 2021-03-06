#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from my_unitest.my_test_style import MyTestRunner
from my_unitest.base_test_case import BaseTestCase


class Dict(dict):

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


class TestDict(BaseTestCase):

    def setUp(self):
        pass

    def test_init(self):
        """测试用例不展示方法名，而展示这串文字"""
        self.println('自定义输出一些文字')
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main(testRunner=MyTestRunner())
